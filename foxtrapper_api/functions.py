from werkzeug.utils import secure_filename
from google.cloud import vision
from google.cloud import storage

import io
import os
import base64


def detect_web_uri(uri):
    """Detects web annotations in the file located in Google Cloud Storage."""
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.web_detection(image=image)
    annotations = response.web_detection

    if annotations.best_guess_labels:
        for label in annotations.best_guess_labels:
            print("\nBest guess label: {}".format(label.label))

    if annotations.pages_with_matching_images:
        print(
            "\n{} Pages with matching images found:".format(
                len(annotations.pages_with_matching_images)
            )
        )

        for page in annotations.pages_with_matching_images:
            print("\n\tPage url   : {}".format(page.url))

            if page.full_matching_images:
                print(
                    "\t{} Full Matches found: ".format(len(page.full_matching_images))
                )

                for image in page.full_matching_images:
                    print("\t\tImage url  : {}".format(image.url))

            if page.partial_matching_images:
                print(
                    "\t{} Partial Matches found: ".format(
                        len(page.partial_matching_images)
                    )
                )

                for image in page.partial_matching_images:
                    print("\t\tImage url  : {}".format(image.url))

    if annotations.web_entities:
        print("\n{} Web entities found: ".format(len(annotations.web_entities)))

        for entity in annotations.web_entities:
            print("\n\tScore      : {}".format(entity.score))
            print("\tDescription: {}".format(entity.description))

    if annotations.visually_similar_images:
        print(
            "\n{} visually similar images found:\n".format(
                len(annotations.visually_similar_images)
            )
        )

        for image in annotations.visually_similar_images:
            print("\tImage url    : {}".format(image.url))

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )


def detect_web(filepath):
    """Detects web annotations given an image."""

    client = vision.ImageAnnotatorClient()

    with open(filepath, "rb") as file:
        content = file.read()

    image = vision.types.Image(content=content)
    response = client.web_detection(image=image)
    annotations = response.web_detection

    result = []

    result.append({"WEB ENTITY SEARCH - START": ""})

    if annotations.best_guess_labels:
        for label in annotations.best_guess_labels:
            result.append({"Best guess label:": str(label.label)})

    if annotations.pages_with_matching_images:
        result.append(
            {
                "Pages with matching images found:": len(
                    annotations.pages_with_matching_images
                )
            }
        )

        for page in annotations.pages_with_matching_images:
            result.append({"Page url:": str(page.url)})

            if page.full_matching_images:
                result.append({"Full Matches found:": len(page.full_matching_images)})

                for image in page.full_matching_images:
                    result.append({"Image url:": str(image.url)})

            if page.partial_matching_images:
                result.append(
                    {"Partial Matches found:": len(page.partial_matching_images)}
                )

                for image in page.partial_matching_images:
                    result.append({"Image url:": str(image.url)})

    if annotations.web_entities:
        result.append({"Web entities found:": len(annotations.web_entities)})

        for entity in annotations.web_entities:
            result.append({"Score:": str(entity.score)})
            result.append({"Description:": str(entity.description)})

    if annotations.visually_similar_images:
        result.append(
            {"Visually similar images found:": len(annotations.visually_similar_images)}
        )

        for image in annotations.visually_similar_images:
            result.append({"Image url:": str(image.url)})

            # print("\tImage url    : {}".format(image.url))

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )

        result.append({"WEB ENTITY SEARCH - END": ""})

    return result


def upload_blob(bucket_name, source_file, destination_blob_name):

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    # blob.upload_from_filename(source_file_name)
    blob.upload_from_filename(source_file)


def file_upload(file):
    filename = secure_filename(file.filename)
    destination = os.path.join(os.getcwd(), "uploads", filename)

    file.save(destination)

    upload_blob("claims-images", destination, filename)

    return destination


def encode_image(data):
    image = data.read()
    encoded_image = base64.b64encode(image)

    return encoded_image


def get_similar_products_file(
    project_id, location, product_set_id, product_category, filepath, filter
):
    """Search similar products to image.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_set_id: Id of the product set.
        product_category: Category of the product.
        file_path: Local file path of the image to be searched.
        filter: Condition to be applied on the labels.
        Example for filter: (color = red OR color = blue) AND style = kids
        It will search on all products with the following labels:
        color:red AND style:kids
        color:blue AND style:kids
    """
    # product_search_client is needed only for its helper methods.
    product_search_client = vision.ProductSearchClient()
    image_annotator_client = vision.ImageAnnotatorClient()

    results = []
    results.append({"LOCAL DATABASE SEARCH - START": ""})

    # Read the image as a stream of bytes.

    with open(filepath, "rb") as file:
        content = file.read()

    # Create annotate image request along with product search feature.
    image = vision.types.Image(content=content)

    # product search specific parameters
    product_set_path = product_search_client.product_set_path(
        project=project_id, location=location, product_set=product_set_id
    )
    product_search_params = vision.types.ProductSearchParams(
        product_set=product_set_path,
        product_categories=[product_category],
        filter=filter,
    )
    image_context = vision.types.ImageContext(
        product_search_params=product_search_params
    )

    # Search products similar to the image.
    response = image_annotator_client.product_search(image, image_context=image_context)

    index_time = response.product_search_results.index_time
    results.append({"Product set index time:": ""})
    results.append({"  seconds:": str(index_time.seconds)})
    results.append({"  nanos:": str(index_time.nanos)})

    res = response.product_search_results.results

    results.append({"Search results:": ""})

    for result in res:
        product = result.product

        results.append({"Score(Confidence):": str(result.score)})
        results.append({"Image name:": str(result.image)})

        results.append({"Product name:": str(product.name)})
        results.append({"Product display name:": str(product.display_name)})
        results.append({"Product description:": str(product.description)})
        results.append({"Product labels:": str(product.product_labels)})

    results.append({"LOCAL DATABASE SEARCH - END": ""})

    return results
