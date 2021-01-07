<template>
  <div id="landing">

  <!-- Navbar Begin -->
    <nav id="navbar" class="docked-nav">
      <div id="navbar-content">
        <div id="logo-div">
          <a href="#landing">
            <p><span class="emphasised-text-gradient"> Robo</span>dokas</p>
          </a>
        </div>
        <div id="menu-div">
          <div id="menu-items-1">
            <ul>
              <a href="#landing"><li id="nav-link-to-main" class="emphasised-text">{{ strings[lang]["navMain"] }}</li></a>
              <a href="#about-section"><li id="nav-link-to-about">{{ strings[lang]["navAbout"] }}</li></a>
              <a href="#contact"><li id="nav-link-to-contact">{{ strings[lang]["navContact"] }}</li></a>
            </ul>
          </div>
          <div id="menu-items-2">
            <ul>
              <router-link v-if="this.$store.getters.isLoggedIn" id="login-link" class="emphasised-text" to="/login"><li><i class="fas fa-cogs"></i> {{ strings[lang]["navDashboard"] }}</li></router-link>
              <router-link v-else id="login-link" class="emphasised-text" to="/login"><li><i class="fas fa-sign-in-alt"></i> {{ strings[lang]["navLogIn"] }}</li></router-link>
              <!-- <a href="#" v-if="this.$store.getters.isLoggedIn" id="logout-link" class="emphasised-text" @click="logOut"><li><i class="fas fa-sign-out-alt"></i> Log Out</li></a> -->
            </ul>
            <div id="lang-select-div">
              <select id="lang-select" v-model="userLangInput" @change="changeLang">
                <option value="en" selected>EN</option>
                <option value="lt">LT</option>
              </select>
              <img :src="'./src/assets/' + lang + '.png'" alt="flag">
            </div>
          </div>
        </div>
      </div>
    </nav>
  <!-- Navbar End -->

  <!-- Main Section -->
    <section id="main">

      <!-- Main Text and CTA -->
      <div id="main-content">

        <div id="logo-div-main">
          <img id="logo-main" src="./assets/logo-colored-alt.png" alt="logo">
          <h1><span class="emphasised-text-gradient"> Robo</span>dokas</h1>
        </div>
        
        <p>{{ strings[lang]["mainSlogan"] }}</p>
        
        <a href="#about-section" id="call-to-action">{{ strings[lang]["mainReadMore"] }} &emsp;<i class="fas fa-chevron-down"></i></a>

      </div>
      <!-- Main Text and CTA End -->

      <!-- Video -->
      <video src="./assets/rbdk-360.mp4" autoplay="true" loop=true muted></video>
      <!-- Video End -->

      <!-- Greyscale Overlay -->
      <div id="bw-overlay"></div>
      <!-- Greyscale Overlay End -->

      <div id="about-section"></div>

    </section>
  <!-- Main Section End -->

  <!-- About Section -->
    <section id="about">
      <div id="about-contents">
        <!-- What is Robodokas -->
        <h2><span class="emphasised-text-alt">{{ strings[lang]["aboutWhat"] }}</span> {{ strings[lang]["aboutIsRd"] }}&trade;</h2>
        <div id="features-div">
          <!-- Features Div -->
          <div class="row">
            <div class="box">
              <div class="icon-div">
                <i id="robot-icon" class="fas fa-robot fa-3x"></i>
              </div>
              <h3>{{ strings[lang]["aboutRoboFiler"] }}</h3>
              <p>{{ strings[lang]["aboutRoboFilerText"] }}</p>
            </div>
            <div class="box">
              <div class="icon-div">
                <i class="fas fa-archive fa-3x"></i>
              </div>
              <h3>{{ strings[lang]["aboutRepo"] }}</h3>
              <p>{{ strings[lang]["aboutRepoText"] }}</p>
            </div>
          </div>
          <div class="row">
            <div class="box">
              <div class="icon-div">
                <i class="fas fa-language fa-3x"></i>
              </div>
              <h3>{{ strings[lang]["aboutTransl"] }}</h3>
              <p>{{ strings[lang]["aboutTranslText"] }}</p>
            </div>
            <div class="box">
              <div class="icon-div">
                <i class="fas fa-drafting-compass fa-3x"></i>
              </div>
              <h3>{{ strings[lang]["aboutTailor"] }}</h3>
              <p>{{ strings[lang]["aboutTailorText"] }}</p>
            </div>
          </div>
          <!-- Features Div End -->
        </div>
        <div id="go-to-contacts" class="animated">
          <a href="#contact">{{ strings[lang]["aboutContact"] }} &emsp;<i class="fas fa-chevron-down"></i></a>
        </div>
        <!-- What is Robodokas End -->
      </div>
    </section>
  <!-- About Section End -->

  <section id="contact-sales">
    <div id="contact-sales-content">
      <div id="animated-text-div">
        <h2 id="animated-text"></h2>
      </div>
      <a id="call-to-action-alt" href="mailto:support@robodokas.com">{{ strings[lang]["contactContact"] }}&ensp;<i class="far fa-envelope"></i></a>
    </div>
    <div id="contact-bezier-ol">
    </div>
  </section>

  <!-- Contact Section -->
    <section id="contact">
      <div id="form-div">
        <div id="form-div-contents">
          <h2>{{ strings[lang]["contactHow"] }} <span class="emphasised-text">{{ strings[lang]["contactToFind"] }}</span>:</h2>
          <div id="requisites">
            <ul>
              <li>{{ strings[lang]["contactAddress"] }}: Ateities g. 20, Vilnius 08303</li>
              <li>{{ strings[lang]["contactPhone"] }}: +370 (673) 12191</li>
              <li>{{ strings[lang]["contactEmail"] }}: <a class="emphasised-text-alt" href="mailto:support@robodokas.com">support@robodokas.com</a></li>
              <br/>
              <li>{{ strings[lang]["contactRegName"] }}: MB "BRObotai"</li>
              <li>{{ strings[lang]["contactCode"] }}: 123456789</li>
              <br/>
              <li>{{ strings[lang]["contactBank"] }}: Swedbank, AB</li>
              <li>{{ strings[lang]["contactIban"] }}: LT49 7300 0100 2377 2144</li>
              <li>{{ strings[lang]["contactBIC"] }}: HABALT22</li>
            </ul>
          </div>
        </div>
      </div>
      <div id="map-div">
        <div id="map"></div>
      </div>
    </section>
  </div>
</template>

<script>
import Typed from 'typed.js'
import firebase from 'firebase'
import mapStyleDark from './mapStyle.json'

export default {
  name: 'landing',
  data() {
    return {
      userLangInput: "en",
      strings: {
        "lt": {
          "navMain": "Pagrindinis",
          "navAbout": "Apie",
          "navContact": "Kontaktai",
          "navLogIn": "Prisijungti",
          "navDashboard": "Skydelis",
          "mainSlogan": "Dokumentų pildymas paprasčiau.",
          "mainReadMore": "Sužinoti daugiau",
          "aboutWhat": "Kas",
          "aboutIsRd": "yra Robodokas",
          "aboutRoboFiler": "Robotinis Dokumentų Pildytojas",
          "aboutRoboFilerText": "Pasirinkite šabloną iš daugybės galimų (mokesčių deklaracijos, įgaliojimai, registracijos formos), įveskite duomenis vieną kartą ir Robodokas pasirūpins duomenų tikrinimu, kopijavimu bei logikos taikymu už jus.",
          "aboutRepo": "Bendra Šablonų Saugojimo Erdvė",
          "aboutRepoText": "Įkelkite aktualiausią dokumento šabloną ir Robodokas saugos jį parankiai jums ir jūsų komandai. Pamirškite apie po ofisą skrajojančius \"ataskaita-v3-galutinė-v2-aktuali.doc\"!",
          "aboutTransl": "Dokumentų Vertėjas",
          "aboutTranslText": "Sunku suprasti teisinių ir organizacijos vidaus dokumentų šablonus, jų reikalavimus? Nesirūpinkite, Robodokas į jūsų pasirinktą kalbą išvers šablone prašomos informacijos turinį.",
          "aboutTailor": "Šablonų Stilistas",
          "aboutTailorText": "Neradote tinkamo standartinio šablono? Jokių problemų - pateikite \"Indivitualaus Šablono\" prašymą ir mes sukursime jį pagal jūsų poreikius! Robodokas juo dalinsis tik su jumis, tad nesirūpinkitė dėl konfidencialumo.",
          "aboutContact": "Pasikalbėkime",
          "contactSlogans": ["Atsisakykite skrupulingo darbo.",
                             "Užtikrinkite savo šablonų aktualumą.",
                             "Pagerinkite savo produktyvumą.",
                             "Užtikrinkite savo dokumentų tikslumą."],
          "contactContact": "Susisiekite",
          "contactHow": "Kaip",
          "contactToFind": "mus rasti",
          "contactAddress": "Adresas",
          "contactPhone": "Tel.",
          "contactEmail": "El. paštas",
          "contactRegName": "Įmonės pav. registre",
          "contactCode": "Įmonės kodas",
          "contactBank": "Bankas",
          "contactIban": "IBAN",
          "contactBIC": "HABALT22"
        },
        "en": {
          "navMain": "Main",
          "navAbout": "About",
          "navContact": "Contact",
          "navLogIn": "Log In",
          "navDashboard": "Dashboard",
          "mainSlogan": "Still paperwork, but more elegant.",
          "mainReadMore": "Read More",
          "aboutWhat": "What",
          "aboutIsRd": "is Robodokas",
          "aboutRoboFiler": "Robotic Filing Assistant",
          "aboutRoboFilerText": "Pick a template from a variety of choices (tax returns, PoAs, registration forms, etc), input details once and Robodokas™ will take care of data validation, copying data and applying business logic where necessary for you.",
          "aboutRepo": "Shared Repository of Templates",
          "aboutRepoText": "Upload the most recent document template and Robodokas will conveniently store it for you or your team to use. Forget about \"report-v3-final-v2-actual.doc\" floating around the office!",
          "aboutTransl": "Document Translator",
          "aboutTranslText": "Having trouble understanding legal or organisation-wide documentation templates and required inputs? No worries, Robodokas™ will translate the content of required inputs to the language of your choice.",
          "aboutTailor": "Template Tailor",
          "aboutTailorText": "Default templates won't cut it? No problem - submit a \"Bespoke Template\" request and we'll tailor one to your needs! Robodokas™ will only share it with you, so no worries about confidentiality.",
          "aboutContact": "Let's talk",
          "contactSlogans": ['Unburden yourself from tedious work.',
                             'Ensure currentness of your documents.',
                             'Enhance your productivity.',
                             'Assure correctness of your documents.'],
          "contactContact": "Contact Us",
          "contactHow": "How to",
          "contactToFind": "find us",
          "contactAddress": "Address",
          "contactPhone": "Phone",
          "contactEmail": "E-mail",
          "contactRegName": "Registered name",
          "contactCode": "Company Code",
          "contactBank": "Bank",
          "contactIban": "IBAN",
          "contactBIC": "HABALT22"

        }
      },
      typed: {}

    }
  },
  computed: {
    lang() {
      return this.$store.getters.getLang
    }
  },
  methods: {
    changeLang() {
      this.$store.commit('langChange', this.userLangInput);
      this.animateMainText();
    },
    animateMainText() {
      const textArray = this.strings[this.lang]['contactSlogans'];

      if (Object.entries(this.typed).length !== 0) {
        this.typed.destroy();
      }

      this.typed = new Typed('#animated-text', {
        strings: textArray,
        startDelay: 800,
        backSpeed: 20,
        typeSpeed: 40,
        backDelay: 1000,
        loop: true}
        );
    },
    initMap() {
      let map = new google.maps.Map(document.getElementById('map'),
                                    {center: {lat: 54.7340409, lng: 25.2590089},
                                     zoom: 17,
                                     styles: mapStyleDark,
                                     zoomControl: true,
                                     mapTypeControl: false,
                                     scaleControl: true,
                                     streetViewControl: false,
                                     rotateControl: false,
                                     fullscreenControl: false
                                    });

      let marker = new google.maps.Marker({
                                           position: {lat: 54.7340409, lng: 25.2590089},
                                           map: map,
                                           title: 'Mykolas Romeris university'
                                           });


    },
    logOut() {
      firebase
        .auth()
        .signOut()
        .then(x => {
          this.$store.commit('logOut')  
          this.$router.push('/login')  
        })
    }
  },
  mounted() {

    if(location.hostname == "robodokas.com" || location.hostname == "www.robodokas.com"){
      this.userLangInput = "en"
    } else {
      this.userLangInput = "lt"
    }

    this.changeLang();

    $(window).scroll(() => {
      let scroll = $(window).scrollTop();

      // console.log(scroll)

      if (scroll > 470) {
        $('#navbar').removeClass('docked-nav').addClass('full-nav')
        $('#logo-div').removeClass('animated fadeOutDown faster')
        $('#logo-div').css('visibility', 'visible')
        $('#logo-div').addClass('animated fadeInUp')
      } else {
        $('#navbar').removeClass('full-nav').addClass('docked-nav')
        $('#logo-div').addClass('animated fadeOutDown faster')
      };

      if (scroll > 889) {
        $('#go-to-contacts').css('visibility', 'visible')
        $('#go-to-contacts').addClass('fadeInUp')
      }

      if (scroll > 1320) {
        $("#nav-link-to-main").removeClass('emphasised-text')
        $("#nav-link-to-about").removeClass('emphasised-text')
        $("#nav-link-to-contact").addClass('emphasised-text')      
      } else if (scroll > 450) {
        $("#nav-link-to-main").removeClass('emphasised-text')
        $("#nav-link-to-about").addClass('emphasised-text')
        $("#nav-link-to-contact").removeClass('emphasised-text')      
      } else {
        $("#nav-link-to-main").addClass('emphasised-text')
        $("#nav-link-to-about").removeClass('emphasised-text')
        $("#nav-link-to-contact").removeClass('emphasised-text')      
      }
    })

    this.animateMainText();
    this.initMap();
  }
}
</script>

<style lang="scss">
  @import url('https://fonts.googleapis.com/css?family=Montserrat&display=swap');

  /* Document */

  $main-font: 'Montserrat', sans-serif;
  $alt-font: 'Raleway', sans-serif;
  // $nav-color: 	#133337;
  $emphasis-color: #ffd700;
  $emphasis-color-alt: #ffa500;
  $white-text-color: #f5f5f5;
  $white-text-color-alt: #EEEEEE;
  $black-text-color: #133337;
  $black-text-color-alt: #2c4c50;
  $black-text-color-alt-2: #242F3E;

  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  html, body {
    color: $white-text-color;
    background: $black-text-color-alt;
    font-family: $main-font; 
    scroll-behavior: smooth;

    a {
      text-decoration: none;
      color: $white-text-color;
      transition: color 0.2s;
    }
  
  }

  .emphasised-text {
    color:	$emphasis-color !important;
    font-weight: bold !important;
    transition: color .3s !important;

  }

  .emphasised-text-alt {
    color:	$emphasis-color-alt;

    font-weight: bold;
    transition: color .3s;
  }

  .emphasised-text-gradient {
    color:	$emphasis-color-alt;
    background: linear-gradient(to bottom, $emphasis-color, $emphasis-color-alt);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: bold;
    transition: color .3s;
  }

  .typed-cursor {
    font-size: 3rem;
  }

  .docked-nav {
    background: linear-gradient(to bottom, $black-text-color-alt-2, rgba(0, 0 , 0, 0) ) !important;
    transition: background .5s;
  }

  .full-nav {
    background: $black-text-color-alt-2 !important;
    transition: background .5s;
  }

  .hidden-logo {
    opacity: 0 !important;
    transition: opacity .5s !important;
  }

  .visible-logo {
    opacity: 1 !important;
    transition: opacity .5s !important;
  }

  #navbar {
    // background:  linear-gradient(to bottom, $nav-color, rgba(0, 0 , 0, 0) );
    height: 5vh;
    position: sticky;
    top: 0;
    z-index: 999;

    #navbar-content {
      max-width: 1800px;
      height: 100%;
      margin: 0 auto;
      padding: 0 2rem;
      display: flex;
      align-items: center;
      justify-content: space-between;

      #logo-div {
        font-size: 1.5rem;
        visibility: hidden;
        flex: 2;
        // opacity: 0;
        
        a {
          display: flex;
          align-items: center;

          img {
            width: 3rem;
          }

          p {
            color: #f5f5f5;
            transition: color 0.2s;
            
            &:hover {
              color: $emphasis-color;
              transition: color 0.2s;
            }
          }
        }
      }

      #menu-div {
        flex: 1;
        display: flex;
        justify-content: space-between;
        font-size: 1rem;
        height: 100%;


        #menu-items-1 {
          flex: 1;
          margin-right: 3rem;
          display: flex;
          justify-content: space-between;

          ul {
            display: flex;
            align-items: center;
            height: 100%;

            li {
              list-style: none;
              padding: 0 .75rem;
              color: $white-text-color;
              transition: color .3s;

              &:hover {
                color: $emphasis-color;
                transition: color .3s;
              }
            }
          }
        }

        #menu-items-2 {
          flex: 1;
          display: flex;
          justify-content: space-evenly;
          align-items: center;

          ul {
            flex: 1;
            display: flex;

            li {
              list-style: none;
              color: $emphasis-color;
              transition: color .3s;
            
              &:hover {
                color: $emphasis-color-alt !important;
                transition: color .3s !important;
              }
            }
          }

          #lang-select-div {
            flex: 1;
            display: flex;
            justify-content: center;;
            align-items: center;
      
            #lang-select {
              background: none;
              border: 1pt solid $emphasis-color;
              border-radius: 5px;
              color: $emphasis-color;
              padding: .25rem;
              outline: none;
              margin-right: .5rem;

              option {
                background: $black-text-color;
              }
            }

            img {
              width: 1.5rem;
              height: 1.5rem;
            }
          }
        }
      }
    }
  }

  #main {
    height: 100vh;
    background: $white-text-color;
    // background: url('./assets/docs-2-bw-2.jpg') no-repeat center center/cover;

    #main-content {
      position: relative;
      max-width: 1800px;
      padding: 0 3rem;
      height: 100%;
      width: 100%;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      z-index: 2;

      #logo-div-main {
        display: flex;
        align-items: center;

        #logo-main {
          width: 8rem;
        }

        h1 {
          font-size: 6rem;
        }

      }

      p {
        font-size: 1.5rem;
        margin-top: .5rem;
      }

      #call-to-action {
        display: block;
        margin-top: 2.25rem;
        background: none;
        color: $emphasis-color; 
        padding: 1.1rem;
        transition-property: background, color, border;
        transition-duration: 0.2s;
        border: 1pt solid $emphasis-color;
        border-radius: 5px;

        &:hover {
          color: $white-text-color;
          border: 1pt solid $emphasis-color-alt;
          background: $emphasis-color-alt;
          transition-property: border, color, background;
          transition-duration: 0.2s;
        }
      }
    }

    video {
      position: absolute;
      top: 0;
      left: 0;
      height: 100%;
      width: 100%;
      object-fit: fill;
      overflow: hidden;
      z-index: 0;
    }

    #bw-overlay {
      background: rgba(0, 0, 0, .6);
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 1;
    }

    #about-section {
      position: absolute;
      left: 0;
      bottom: 0;
      width: 100%;
      height: 5vh;
    }

  }

  /* About Section */

  #about {
    height: 90vh;
    color: $black-text-color;
    background: url('./assets/bezier-4.svg');
    background-repeat: no-repeat;
    background-size: 100%, 100%;
    background-position: 0;
    background-color: $white-text-color;

    #about-contents {
      height: 100%;
      display: flex;
      max-width: 1800px;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      margin: 0 auto;
      padding: 0 3rem;
      z-index: 999;

      h2 {
        flex: 1;
        margin-top: 1rem;
        text-align: center;
      }

      #features-div {
        flex: 8;
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        align-items: center;
        margin-bottom: 3rem;

        .row {
          display: flex;
          flex-direction: row;
          justify-content: space-between;

          .box {
            display: flex;
            flex-direction: column;
            align-items: center;
            flex: 1;
            padding: 0 3rem;

            .icon-div {
              background: linear-gradient(to bottom, $emphasis-color, $emphasis-color-alt);
              border-radius: 50%;
              line-height: 5rem;
              height: 6rem;
              width: 6rem;
              display: flex;
              align-items: center;
              justify-content: center;
              margin-bottom: 1rem;

              #robot-icon {
                position: relative;
                bottom: 4px;
              }
            }

            h3 {
              margin-bottom: 1rem;
            }

            p {
              text-align: justify;
              width: 80%;
            }
          }
        }
      }

      #go-to-contacts {
        flex: 1;
        visibility: hidden;

          a {
            display: block;
            margin-bottom: 5rem;
            border: 1pt solid $emphasis-color-alt;
            border-radius: 5px;
            color: $emphasis-color-alt; 
            padding: 1.1rem;
            transition-property: background, color;
            transition-duration: 0.2s;

            &:hover {
              color: $white-text-color;
              background: $emphasis-color-alt;
              transition-property: color, background;
              transition-duration: 0.2s;
            }
          }
      }
    }
  }

  #contact-sales {
    height: 45vh;
    color: $black-text-color;
    background: linear-gradient(to bottom, $emphasis-color, $emphasis-color-alt); // $emphasis-color-alt; $white-text-color-alt;
    position: relative;

    #contact-sales-content {
      max-width: 1800px;
      margin: 0 auto;
      height: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      z-index: 1;

      #animated-text-div {
        display: flex;
        align-items: flex-end;
        z-index: 1;

        h2 {
          font-size: 3rem;
        }
      }

      #call-to-action-alt {
        display: block;
        margin-top: 2.25rem;
        background: rgba(#008000, .8);
        color: $white-text-color;
        border-radius: 5px;
        padding: 1.25rem 1.5rem;
        transition-property: background, color;
        transition-duration: .3s;
        font-size: 1.15rem;
        z-index: 1;

        &:hover {
          color: $white-text-color;
          background: #065535;
          transition-property: color, background;
          transition-duration: .3s;
        }
      }
    }

    #contact-bezier-ol {
      width: 100%;
      height: 100%;
      position: absolute;
      left: 0;
      top: 0;
      background: url('./assets/bezier-6.svg');
      background-repeat: no-repeat;
      background-size: 100%, 100%;
      background-position: 0;
      z-index: 0;

    }
  }

  /* Contact Section */

  #contact {
    height: 50vh;
    background: $black-text-color-alt;
    display: flex;

    #form-div {
      flex: 1;
      background-color: $black-text-color-alt-2;
      
      // background: url('./assets/bezier-7.svg');
      // background-repeat: no-repeat;
      // background-size: cover;
      // background-position: 0;

      #form-div-contents {
        width: 100%;
        height: 100%;
        display: flex;
        padding: 0 3rem;
        flex-direction: column;
        justify-content: space-evenly;


        h2 {
          text-align: center;
        }

        #requisites {
          ul {
            list-style: none;

            li {
              font-size: 1.15rem;
            }
          }
        }
      }

    }

    #map-div {
      flex: 2;

      #map {
        height: 100%;
      }
    }


  }


</style>
