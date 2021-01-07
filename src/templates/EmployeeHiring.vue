<template>
  <div id="vmi-eds">
    <!-- Navigation -->
    <div id="nav-wrapper">
      <nav id="dashboard-nav">
        <div id="nav-content">
          <router-link id="dashboard-back-button" class="emphasised-text" to="/dashboard">
            <i class="far fa-arrow-alt-circle-left"></i>
            {{ this.strings[lang]['back'] }}
          </router-link>
          <a
            href="#"
            v-if="this.$store.getters.isLoggedIn"
            id="dashboard-ogout-button"
            class="emphasised-text"
            @click="logOut"
          >
            <i class="fas fa-sign-out-alt"></i>
            {{ this.strings[lang]['logOut'] }}
          </a>
        </div>
      </nav>
    </div>
    <!-- Template Area -->
    <section id="report-area">
      <div id="control-side" class="animated delay-1s fadeIn">
        <h1>
          {{ this.strings[lang]['fillIn'] }}
          <span
            class="emphasised-text"
          >{{ this.strings[lang]['required'] }}</span>
          {{ this.strings[lang]['inputs'] }}:
        </h1>
        <div id="inputs">
          <h2>{{ this.strings[lang]['employeeName'] }}:</h2>
          <input
            type="text"
            name="employee-name-control"
            id="employee-name-control"
            v-model="employeeName"
            required
            @keyup.enter="generateVmiEds"
          />
          <h2>{{ this.strings[lang]['employeeId'] }}:</h2>
          <input
            type="text"
            name="employee-id-control"
            id="employee-id-control"
            v-model="employeeId"
            maxlength="20"
            @keyup.enter="generateVmiEds"
            required
          />
          <h2>{{ this.strings[lang]['employeeAddress'] }}:</h2>
          <input
            type="text"
            v-model="employeeAddress"
            name="employee-address-control"
            id="employee-address-control"
            maxlength="30"
            @keyup.enter="generateVmiEds"
            required
          />
          <h2>{{ this.strings[lang]['employeePhone'] }}:</h2>
          <input
            type="text"
            v-model="employeePhone"
            name="employee-phone-control"
            id="employee-phone-control"
            @keyup.enter="generateVmiEds"
            maxlength="20"
          />
          <h2>{{ this.strings[lang]['companyName'] }}:</h2>
          <input
            type="text"
            v-model="companyName"
            name="company-name-control"
            id="company-name-control"
            maxlength="30"
            @keyup.enter="generateVmiEds"
            required
          />
          <h2>{{ this.strings[lang]['directorName'] }}:</h2>
          <input
            type="text"
            v-model="directorName"
            name="director-name-control"
            id="director-name-control"
            maxlength="20"
            @keyup.enter="generateVmiEds"
            required
          />
          <h2>{{ this.strings[lang]['date'] }}:</h2>
          <input
            type="date"
            v-model="date"
            name="date-control"
            id="date-control"
            @keyup.enter="generateVmiEds"
            required
          />
          <h2>{{ this.strings[lang]['location'] }}:</h2>
          <input
            type="text"
            v-model="loc"
            name="location-control"
            id="location-control"
            maxlength="30"
            @keyup.enter="generateVmiEds"
            required
          />
          <h2>{{ this.strings[lang]['role'] }}:</h2>
          <input
            type="text"
            v-model="role"
            name="role-control"
            id="role-control"
            maxlength="20"
            @keyup.enter="generateVmiEds"
            required
          />
          <h2>{{ this.strings[lang]['startingDate'] }}:</h2>
          <input
            type="date"
            v-model="startingDate"
            name="starting-date-control"
            id="starting-date-control"
            @keyup.enter="generateVmiEds"
            required
          />
        </div>
        <input
          id="mail-btn"
          type="button"
          :value="this.strings[lang]['mailMe']"
          class="contact-btn"
          @click="generateVmiEds"
        />
      </div>
      <div id="template-side" class="animated delay-1s fadeIn">
        <div id="pre-requisites">
          <div id="line-one">
            <input
              type="text"
              name="employee-name"
              id="employee-name"
              :placeholder="this.strings[lang]['employeeName']"
              v-model="employeeName"
              required
            />
          </div>
          <div id="line-two">
            <span>A. k.</span>
            <input
              type="text"
              name="employee-id"
              id="employee-id"
              :placeholder="this.strings[lang]['employeeId']"
              v-model="employeeId"
              required
            />
            <span>,</span>
            <input
              type="text"
              name="employee-address"
              id="employee-address"
              :placeholder="this.strings[lang]['employeeAddress']"
              v-model="employeeAddress"
              required
            />
            <span>, tel.</span>
            <input
              type="text"
              name="employee-phone"
              id="employee-phone"
              :placeholder="this.strings[lang]['employeePhone']"
              v-model="employeePhone"
              required
            />
          </div>
          <div id="director-section">
            <div id="row-one">
              <input
                type="text"
                name="company-name"
                id="company-name"
                :placeholder="this.strings[lang]['companyName']"
                v-model="companyName"
                required
              />
            </div>
            <div id="row-two">
              <span>direktoriui (-ei)</span>
              <input
                type="text"
                name="director-name"
                id="director-name"
                :placeholder="this.strings[lang]['directorName']"
                v-model="directorName"
                required
              />
            </div>
          </div>
        </div>
        <h1 id="main-heading">
          PRAŠYMAS
          <br />PRIIMTI Į DARBĄ
        </h1>
        <div id="date-and-reg-div">
          <input
            type="text"
            name="date"
            id="date"
            :placeholder="this.strings[lang]['date']"
            v-model="date"
            required
          />
        </div>
        <div id="location-div">
          <input
            type="text"
            name="location"
            id="location"
            :placeholder="this.strings[lang]['location']"
            v-model="loc"
            required
          />
        </div>

        <div id="paragraph-one">
          <span>&emsp;&emsp;Prašau priimti mane dirbti</span>
          <input
            type="text"
            v-model="role"
            name="role"
            id="role"
            :placeholder="this.strings[lang]['role']"
            required
          />
          <span>nuo</span>
          <input
            type="text"
            v-model="startingDate"
            name="starting-date"
            id="starting-date"
            :placeholder="this.strings[lang]['startingDate']"
            required
          />
          <span>.</span>
        </div>
        <div id="paragraph-two">
          <input
            type="text"
            v-model="employeeName"
            name="employee-name-2"
            id="employee-name-2"
            :placeholder="this.strings[lang]['employeeName']"
            required
          />
        </div>
        <div id="page-separator"></div>
        <div id="npd-requisites-one">
          <input
            type="text"
            v-model="role"
            name="role"
            id="role"
            :placeholder="this.strings[lang]['role']"
            required
          />
          <input
            type="text"
            name="employee-name"
            id="employee-name"
            :placeholder="this.strings[lang]['employeeName']"
            v-model="employeeName"
            required
          />
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "VmiEds",
  data() {
    return {
      employeeName: "",
      employeeId: "",
      employeeAddress: "",
      employeePhone: "",
      companyName: "",
      directorName: "",
      date: "",
      loc: "",
      role: "",
      startingDate: "",
      taxPayerName: "",
      taxPayerCode: "",
      taxPayerRepName: "",
      taxPayerRepBasis: "",
      strings: {
        lt: {
          back: "Atgal į šablonus",
          logOut: "Atsijungti",
          fillIn: "Užpildykite",
          required: "privalomus",
          inputs: "laukus",
          employeeName: "Darbuotojo vardas ir pavardė",
          employeeId: "Darbuotojo asmens kodas",
          employeeAddress: "Darbuotojo adresas",
          employeePhone: "Darbuotojo tel. Nr.",
          companyName: "Įmonės pavadinimas",
          directorName: "Direktoriaus/įgal. asm. vardas, pavardė",
          date: "Dokumento data",
          location: "Vieta",
          // taxPayerName: "Mokesčių mokėtojo vardas/pavadinimas",
          // taxPayerId: "Mokesčių mokėtojo kodas",
          // repName: "Atstovaujantis asmuo ir jo pareigos",
          // repBasis: "Atstovavimo pagrindas",
          role: "Darbuotojo pareigos",
          startingDate: "Pradžios data",
          mailMe: "Atsiųsti man šį dokumentą",
          fillInAlert: "Užpildykite privalomus laukus",
          sendConfirm: "Sugeneruoti ir persiųsti šį dokumentą į jūsų el. paštą?"
        },
        en: {
          back: "Back to Templates",
          logOut: "Log Out",
          fillIn: "Fill in",
          required: "required",
          inputs: "inputs",
          employeeName: "Employee's full name",
          employeeId: "Employee's ID",
          employeeAddress: "Employee's address",
          employeePhone: "Employee's phone number",
          companyName: "Name of the company",
          directorName: "Director's/representative's full name",
          date: "Document date",
          location: "Location",
          // taxPayerName: "Taxpayer's full or legal name",
          // taxPayerId: "Taxpayer's ID number (code)",
          // repName: "Representative's role and full name",
          // repBasis: "Representative's role and full name",
          role: "Role",
          startingDate: "Starting date",
          mailMe: "Mail me this report",
          fillInAlert: "Fill in all required inputs",
          sendConfirm: "Generate and send this report to your email?"
        }
      }
    };
  },
  computed: {
    lang() {
      return this.$store.getters.getLang;
    }
  },
  mounted() {
    // $(document).on("keypress", e => {
    //   if (e.which == 13) {
    //     $("#mail-btn").click();
    //     $("#mail-btn").attr("disabled", true);
    //   }
    // });
  },
  methods: {
    logOut() {
      firebase
        .auth()
        .signOut()
        .then(x => {
          this.$store.commit("logOut");
          this.$router.push("/login");
        });
    },
    generateVmiEds() {
      let prompt = false;

      const Url = "https://robodokas-api.herokuapp.com/VmiEds";
      const Data = {
        user: this.$store.getters.getCurrentUser,
        date: this.date,
        loc: this.loc,
        taxPayerName: this.taxPayerName,
        taxPayerCode: this.taxPayerCode,
        taxPayerRepName: this.taxPayerRepName,
        taxPayerRepBasis: this.taxPayerRepBasis
      };

      if (
        Data.date == "" ||
        Data.loc == "" ||
        Data.taxPayerName == "" ||
        Data.taxPayerCode == "" ||
        Data.taxPayerRepName == "" ||
        Data.taxPayerRepBasis == ""
      ) {
        alert(this.strings[this.lang]["fillInAlert"]);
        // $("#mail-btn").attr("disabled", false);
      } else {
        prompt = confirm(this.strings[this.lang]["sendConfirm"]);
        // $("#mail-btn").attr("disabled", true);
      }

      if (prompt == true) {
        $.ajax({
          url: Url,
          data: JSON.stringify(Data),
          type: "POST",
          contentType: "application/json",
          success: response => {
            console.log(response);
          },
          error: error => {
            console.log(error);
          }
        });

        this.$store.commit("reportSentSwitch");

        setTimeout(() => {
          this.$store.commit("reportSentSwitch");
        }, 10000);

        this.$router.push("/dashboard");
      }
    }
  }
};
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css?family=Montserrat&display=swap");

$main-font: "Montserrat", sans-serif;
$black-text-color: #133337;
$black-text-color-alt: #2c4c50;
$black-text-color-alt-2: #242f3e;
$white-text-color: #f5f5f5;
$emphasis-color: #ffd700;
$emphasis-color-alt: #ffa500;

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html,
body {
  background: $black-text-color-alt !important;
  color: $white-text-color !important;
  font-family: $main-font;
  scroll-behavior: smooth;

  a {
    text-decoration: none;
  }

  .emphasised-text {
    color: $emphasis-color !important;
    font-weight: bold !important;
    transition: color 0.3s !important;
  }

  .emphasised-text-alt {
    color: $emphasis-color-alt;
    font-weight: bold;
    transition: color 0.3s;
  }

  .emphasised-text-gradient {
    color: $emphasis-color-alt;
    background: linear-gradient(
      to bottom,
      $emphasis-color,
      $emphasis-color-alt
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: bold;
    transition: color 0.3s;
  }
}

/* Navigation */
#dashboard-nav {
  height: 5vh;

  #nav-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 100%;
    padding: 0 3rem;
    max-width: 1800px;
    margin: 0 auto;

    a {
      color: $emphasis-color !important;
      transition: color 0.3s;
      display: block;

      &:hover {
        color: $white-text-color !important;
        transition: color 0.3s;
      }
    }
  }
}

/* Report Area */
#report-area {
  display: flex;
  justify-content: center;
  align-items: center;
  max-width: 1800px;
  margin: 0 auto;
  padding: 0 3rem;
  height: 93vh;

  #control-side {
    width: 33.3%;
    height: 88vh;
    background: $black-text-color-alt-2;
    padding: 2rem 3rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;

    h1 {
      font-size: 1.5rem;
      flex: 1;
    }

    #inputs {
      flex: 8;
      // display: flex;
      // flex-direction: column;
      // justify-content: center;
      overflow-x: hidden;
      overflow-y: scroll;
      padding-right: 1rem;
      margin-bottom: 1rem;

      h2 {
        font-size: 1.2rem;
      }

      input[type="text"],
      input[type="date"] {
        width: 100%;
        height: 2.5rem;
        margin-bottom: 1.3rem;
        padding: 0.5rem;
        font-family: $main-font;
        font-size: 1.1rem;
        background: $white-text-color;
        border: 2pt solid rgba(0, 255, 0, 0.75);
        transition: border 0.4s;
      }

      input:invalid {
        border: 2pt solid rgba(255, 0, 0, 0.75);
        transition: border 0.4s;
      }

      input:focus {
        outline: none;
      }
    }

    .contact-btn {
      flex: 1;
      display: block;
      border: none;
      background: $emphasis-color;
      color: $black-text-color;
      font-family: $main-font;
      width: 100%;
      padding: 0.8rem;
      font-size: 1.1rem;
      transition-property: background, color;
      transition-duration: 0.2s;
      cursor: pointer;
      border-radius: 5px;

      &:hover {
        background: $emphasis-color-alt;
        // color: #f5f5f5;
        transition-property: background, color;
        transition-duration: 0.2s;
      }

      &:focus {
        outline: none;
      }
    }
  }
}

/* Template Side (Right) */
#template-side {
  font-family: "Times New Roman", Times, serif;
  width: 66.6%;
  height: 88vh;
  overflow-y: scroll;
  overflow-x: hidden;
  padding: 3rem;
  background: $white-text-color;
  color: $black-text-color;
  line-height: 1.75rem;
  border: 2rem solid $black-text-color-alt-2;

  #page-separator {
    height: 3rem;
    width: 100%;
    border-bottom: 1px dotted $black-text-color;
  }

  input {
    text-align: center;
    font-size: 0.8rem;
    padding: 0.5rem;
    border: none;
    border-radius: 5rem;
    background: #f5f5f5;
    font-size: 0.75rem;
    border: 1pt solid rgba(0, 255, 0, 0.75);
    transition: border 0.4s;

    &:invalid {
      border: 1pt solid rgba(255, 0, 0, 0.75);
      transition: border 0.4s;
    }

    &:focus {
      outline: none;
    }
  }

  #pre-requisites {
    #line-one {
      text-align: center;

      input {
        width: 20rem;
      }
    }

    #line-two {
      text-align: center;
      margin-top: 0.5rem;

      #employee-address {
        width: 20rem;
      }
    }

    #director-section {
      margin-top: 2rem;

      #row-one {
        input {
          width: 20rem;
        }
      }

      #row-two {
        margin-top: 0.5rem;

        input {
          width: 13.5rem;
        }
      }
    }
  }

  #main-heading {
    font-size: 1.3rem;
    text-align: center;
    margin-top: 2rem;
    margin-bottom: 1.5rem;
  }

  #date-and-reg-div {
    text-align: center;
    margin-bottom: 0.5rem;

    #date {
      width: 10rem;
    }
  }

  #location-div {
    text-align: center;
    margin-bottom: 1.7rem;

    #location {
      width: 20rem;
    }
  }

  h2 {
    text-align: center;
    font-size: 1.2rem;
    margin-bottom: 1.5rem;
  }

  #paragraph-one {
    margin-top: 2rem;
    margin-bottom: 2rem;
    text-align: justify;

    #role {
      width: 10rem;
    }

    #starting-date {
      width: 10rem;
    }
  }

  #paragraph-two {
    margin-top: 10rem;
    margin-bottom: 2rem;
    text-align: right;
  }

  #npd-requisites-one {
  }
}
</style>
