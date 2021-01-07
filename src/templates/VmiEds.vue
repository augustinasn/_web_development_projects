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
          <h2>{{ this.strings[lang]['date'] }}:</h2>
          <input type="date" name="date-control" id="date-control" v-model="date" required />
          <h2>{{ this.strings[lang]['location'] }}:</h2>
          <input
            type="text"
            name="location-control"
            id="location-control"
            v-model="loc"
            maxlength="30"
            @keyup.enter="generateVmiEds"
            required
          />
          <h2>{{ this.strings[lang]['taxPayerName'] }}:</h2>
          <input
            type="text"
            v-model="taxPayerName"
            name="tax-payer-name"
            id="tax-payer-name"
            maxlength="30"
            @keyup.enter="generateVmiEds"
            required
          />
          <h2>{{ this.strings[lang]['taxPayerId'] }}:</h2>
          <input
            type="text"
            v-model="taxPayerCode"
            name="tax-payer-code"
            id="tax-payer-code"
            @keyup.enter="generateVmiEds"
            maxlength="20"
            required
          />
          <h2>{{ this.strings[lang]['repName'] }}:</h2>
          <input
            type="text"
            v-model="taxPayerRepName"
            name="tax-payer-representative-name"
            id="tax-payer-representative-name"
            maxlength="30"
            @keyup.enter="generateVmiEds"
            required
          />
          <h2>{{ this.strings[lang]['repBasis'] }}:</h2>
          <input
            type="text"
            v-model="taxPayerRepBasis"
            name="tax-payer-representation-basis"
            id="tax-payer-representation-basis"
            maxlength="30"
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
        <h1 id="main-heading">DOKUMENTŲ TEIKIMO ELEKTRONINIU BŪDU SUTARTIS</h1>
        <div id="date-and-reg-div">
          <input
            type="text"
            name="date"
            id="date"
            :placeholder="this.strings[lang]['date']"
            v-model="date"
            required
          />
          <span>Nr.</span>
          <span>________________________</span>
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
        <h2 class="heading">I. SUTARTIES ŠALYS</h2>
        <div id="paragraph-one">
          <em>&emsp;&emsp;Vilniaus apskrities valstybinė mokesčių inspekcija</em>
          <span>, kurią atstovauja _____________________________ veikiantis (-i) pagal</span>
          <em>Vilniaus apskrities valstybinės mokesčių inspekcijos viršininko 2008 m. gegužės 30 d. įsakymą Nr. (1.1)-1-170 (kartu su 2010 m. birželio 21 d. Nr. (1.1)-1-143 įsakymu)</em>
          <span>(toliau – mokesčių administratorius) ir</span>
          <input
            type="text"
            v-model="taxPayerName"
            name="tax-payer-name"
            id="tax-payer-name"
            :placeholder="this.strings[lang]['taxPayerName']"
            required
          />
          <input
            type="text"
            v-model="taxPayerCode"
            name="tax-payer-code"
            id="tax-payer-code"
            :placeholder="this.strings[lang]['taxPayerId']"
            required
          />
          <span>(toliau – mokesčių mokėtojas), kurį (-ią) atstovauja</span>
          <input
            type="text"
            v-model="taxPayerRepName"
            name="tax-payer-representative-name"
            id="tax-payer-representative-name"
            :placeholder="this.strings[lang]['repName']"
            required
          />
          <span>veikiantis (-i) pagal</span>
          <input
            type="text"
            v-model="taxPayerRepBasis"
            name="tax-payer-representation-basis"
            id="tax-payer-representation-basis"
            :placeholder="this.strings[lang]['repBasis']"
            required
          />
          <span>sudarė šią Dokumentų teikimo elektroniniu būdu sutartį (toliau – sutartis).</span>
        </div>
        <h2 class="heading">II. SUTARTIES OBJEKTAS</h2>
        <div id="paragraph-two">
          <span>&emsp;&emsp;1. Sutartis nustato mokesčių mokėtojo ir mokesčių administratoriaus santykius teikiant ir priimant dokumentus elektroniniu būdu per Valstybinės mokesčių inspekcijos Elektroninio deklaravimo informacinę sistemą (toliau – EDS).</span>
          <br />
          <span>&emsp;&emsp;2. Dokumentų, dėl kurių teikimo elektroniniu būdu šalys susitaria, formų sąrašas skelbiamas EDS svetainėje.</span>
        </div>
        <h2>III. ŠALIŲ TEISĖS IR PAREIGOS</h2>
        <div id="paragraph-three">
          <span>&emsp;&emsp;3. Mokesčių mokėtojas privalo:</span>
          <br />
          <span>&emsp;&emsp;3.1. prieš pradėdamas teikti dokumentus elektroniniu būdu, susipažinti su Dokumentų teikimo elektroniniu būdu taisyklėmis (toliau – taisyklės);</span>
          <br />
          <span>&emsp;&emsp;3.2. per 5 darbo dienas mokesčių administratoriui pateikti atitinkamai užpildytą sutarties priedą „Duomenys apie Elektroninio deklaravimo informacinės sistemos vartotoją“ (toliau – sutarties priedas) tais atvejais, kai nutraukiami ar keičiami EDS vartotojo įgaliojimai teikti dokumentus ir/arba atlikti kitus su teikiamais dokumentais susijusius veiksmus.</span>
          <br />
          <span>&emsp;&emsp;4. Mokesčių mokėtojas įsipareigoja:</span>
          <br />
          <span>&emsp;&emsp;4.1. teikti teisingus duomenis teisės aktų nustatytais terminais;</span>
          <br />
          <span>&emsp;&emsp;4.2. teikiant dokumentus elektroniniu paštu, naudoti tik EDS įregistruotą elektroninio pašto adresą;</span>
          <br />
          <span>&emsp;&emsp;4.3. EDS vartotojo (-ų) asmens duomenis naudoti tik su jo(-ų) sutikimu elektroninių dokumentų teikimo ir/ar deklaravimo tikslais.</span>
          <br />
          <span>&emsp;&emsp;5. Mokesčių administratorius turi teisę nepriimti dokumento, jeigu jis neatitinka elektroniniu būdu teikiamiems dokumentams keliamų pildymo ir pateikimo reikalavimų.</span>
          <br />
          <span>&emsp;&emsp;6. Mokesčių administratorius įsipareigoja:</span>
          <br />
          <span>&emsp;&emsp;6.1. konsultuoti mokesčių mokėtoją dokumentų teikimo elektroniniu būdu klausimais;</span>
          <br />
          <span>&emsp;&emsp;6.2. gavęs dokumentą elektroniniu būdu informuoti mokesčių mokėtoją apie dokumento priėmimą EDS;</span>
          <br />
          <span>&emsp;&emsp;6.3. elektroniniu būdu pateiktų dokumentų duomenis ir kitą susijusią informaciją laikyti paslaptyje. Informaciją teikti teisės aktų nustatyta tvarka.</span>
          <br />
        </div>
        <h2>IV. ŠALIŲ ATSAKOMYBĖ</h2>
        <div id="paragraph-four">
          <span>&emsp;&emsp;7. Mokesčių administratorius teisės aktų nustatyta tvarka atsako už mokesčių mokėtojo elektroniniu būdu pateiktų dokumentų saugojimą.</span>
          <br />
          <span>&emsp;&emsp;8. Mokesčių administratorius neatsako už tai, kad dėl informacinių ryšių technologijų gedimų mokesčių mokėtojas negalės prisijungti prie EDS arba kad dėl tokių gedimų bus prarasti ar iškraipyti duomenys jų pateikimo metu.</span>
          <br />
          <span>
            &emsp;&emsp;9. Nei viena iš šalių neatsako už visišką ar dalinį įsipareigojimų neįvykdymą, jeigu ji įrodo, kad įsipareigojimų neįvykdė dėl nenugalimos jėgos (f
            <em>orce majeure</em>) aplinkybių. Įrodžius nenugalimos jėgos (f
            <em>orce majeure</em>) aplinkybes, šalys vadovaujasi Lietuvos Respublikos civilinio kodekso (Žin., 2000, Nr. 74-2262) nuostatomis, Atleidimo nuo atsakomybės esant nenugalimos jėgos (f
            <em>orce majeure</em>) aplinkybėms taisyklėmis, patvirtintomis Lietuvos Respublikos Vyriausybės 1996 m. liepos 15 d. nutarimu Nr. 840 (Žin., Nr. 1996, Nr. 68-1652), ir Nenugalimos jėgos (f
            <em>orce majeure</em>) aplinkybes liudijančių pažymų išdavimo tvarka, patvirtinta Lietuvos Respublikos Vyriausybės 1997 m. kovo 13 d. nutarimu Nr. 222 (Žin., 1997, Nr. 24-556).
          </span>
          <br />
          <span>&emsp;&emsp;10. Neužtikrinus identifikavimo EDS priemonių saugumo, perdavus jas tretiesiems asmenims ir/ar laiku nepranešus apie tai mokesčių administratoriui, už pasekmes atsako mokesčių mokėtojas.</span>
          <br />
        </div>
        <h2>V. SUTARTIES GALIOJIMAS, NUTRAUKIMAS, KEITIMAS</h2>
        <div id="paragraph-five">
          <span>&emsp;&emsp;11. Sutartis įsigalioja nuo jos pasirašymo ir/ar patvirtinimo EDS dienos ir yra neterminuota.</span>
          <br />
          <span>&emsp;&emsp;12. Mokesčių administratorius turi teisę vienašališkai keisti sutarties sąlygas, apie tai informavęs mokesčių mokėtoją prieš 15 kalendorinių dienų.</span>
          <br />
          <span>&emsp;&emsp;13. Sutarties duomenys keičiami ir/arba papildomi, pateikiant naują sutarties priedą.</span>
          <br />
          <span>&emsp;&emsp;14. Sutarties pakeitimai ir papildymai galioja sudaryti raštu ir pasirašyti abiejų šalių arba sudaryti ir patvirtinti per EDS, išskyrus 12 punkte nurodytą atvejį.</span>
          <br />
          <span>&emsp;&emsp;15. Kiekviena iš šalių turi teisę nutraukti sutartį. Apie tai šalis raštu turi įspėti kitą šalį prieš 15 darbo dienų. Jeigu mokesčių mokėtojas pažeidžia sutarties sąlygas, mokesčių administratorius turi teisę nutraukti sutartį nesilaikydamas šiame punkte nustatyto įspėjimo termino.</span>
          <br />
        </div>
        <h2>VI. BAIGIAMOSIOS NUOSTATOS</h2>
        <div id="paragraph-six">
          <span>&emsp;&emsp;16. Atvejais, kurių nenumato ši sutartis, šalys vadovaujasi galiojančiais Lietuvos Respublikos teisės aktais ir taisyklėmis.</span>
          <br />
          <span>&emsp;&emsp;17. Iškilusius ginčus dėl sutarties vykdymo šalys sprendžia derybų būdu. Jeigu ginčo nepavyksta išspręsti derybų būdu, kiekviena šalis turi teisę ginčą spręsti Lietuvos Respublikos įstatymų nustatyta tvarka.</span>
          <br />
          <span>&emsp;&emsp;18. Sutartis sudaroma ir pasirašoma lietuvių kalba dviem vienodą juridinę galią turinčiais egzemplioriais, po vieną kiekvienai šaliai.</span>
          <br />
        </div>
        <h2>VII. ŠALIŲ REKVIZITAI</h2>
        <div id="paragraph-seven">
          <div id="tax-administrator-requisites-one">
            <span>
              <strong>Mokesčių administratorius</strong>
            </span>
            <br />
            <span>Vilniaus apskrities valstybinė mokesčių inspekcija, kodas 188728821</span>
            <br />
            <span>Ulonų g. 2, Vilnius, LT-01509,</span>
            <br />
            <span>Tel.: 1882, (8 5) 268 7621, (8 5) 271 4801 faks. (8 5) 262 1906</span>
          </div>
          <div id="tax-administrator-requisites-two">
            <div id="row-one">
              <span>_______________________</span>
              <span>_______________________</span>
              <span>_______________________</span>
            </div>
            <div id="row-two">
              <span>
                <sup>(pareigų pavadinimas)</sup>
              </span>
              <span>
                <sup>(parašas)</sup>
              </span>
              <span>
                <sup>(vardas, pavardė)</sup>
              </span>
            </div>
          </div>
        </div>
        <div id="paragraph-eight">
          <br />
          <span>
            <strong>Mokesčių mokėtojas</strong>
          </span>
          <br />
          <input
            type="text"
            v-model="taxPayerName"
            name="tax-payer-name-two"
            id="tax-payer-name-two"
            :placeholder="this.strings[lang]['taxPayerName']"
            required
          />
          <input
            type="text"
            v-model="taxPayerCode"
            name="tax-payer-code-two"
            id="tax-payer-code-two"
            :placeholder="this.strings[lang]['taxPayerId']"
            required
          />
          <br />
          <input
            type="text"
            name="location-two"
            id="location-two"
            :placeholder="this.strings[lang]['location']"
            v-model="loc"
            required
          />
          <div id="tax-payer-requisites-final">
            <div id="tax-payer-requisites-final-row-1">
              <span>_______________________</span>
              <span>_______________________</span>
              <input
                type="text"
                v-model="taxPayerRepName"
                name="tax-payer-representative-name-two"
                id="tax-payer-representative-name-two"
                :placeholder="this.strings[lang]['repName']"
                required
              />
            </div>
            <div id="tax-payer-requisites-final-row-2">
              <span>
                <sup>(pareigų pavadinimas)</sup>
              </span>
              <span>
                <sup>(parašas)</sup>
              </span>
              <span>
                <sup>(vardas, pavardė)</sup>
              </span>
            </div>
          </div>
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
      date: "",
      loc: "",
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
          date: "Data",
          location: "Vieta",
          taxPayerName: "Mokesčių mokėtojo vardas/pavadinimas",
          taxPayerId: "Mokesčių mokėtojo kodas",
          repName: "Atstovaujantis asmuo ir jo pareigos",
          repBasis: "Atstovavimo pagrindas",
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
          date: "Date",
          location: "Location",
          taxPayerName: "Taxpayer's full or legal name",
          taxPayerId: "Taxpayer's ID number (code)",
          repName: "Representative's role and full name",
          repBasis: "Representative's role and full name",
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
  height: 95vh;

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
      display: flex;
      flex-direction: column;
      justify-content: center;

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
  overflow: scroll;
  padding: 3rem;
  background: $white-text-color;
  color: $black-text-color;
  line-height: 1.75rem;
  border: 2rem solid $black-text-color-alt-2;

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

  #main-heading {
    font-size: 1.3rem;
    text-align: center;
    margin-bottom: 1.5rem;
  }

  #date-and-reg-div {
    text-align: center;
    margin-bottom: 0.5rem;

    #date {
      width: 7rem;
    }

    #reg-no {
      width: 12rem;
    }
  }

  #location-div {
    text-align: center;
    margin-bottom: 1.7rem;

    #location {
      width: 21rem;
    }
  }

  h2 {
    text-align: center;
    font-size: 1.2rem;
    margin-bottom: 1.5rem;
  }

  #paragraph-one {
    margin-bottom: 2rem;
    text-align: justify;

    #tax-payer-name {
      width: 20rem;
    }

    #tax-payer-code {
      width: 15rem;
    }

    #tax-payer-representative-name {
      width: 15rem;
    }

    input {
      height: 1.5rem;
    }
  }

  #paragraph-two {
    margin-bottom: 2rem;
    text-align: justify;
  }

  #paragraph-three {
    margin-bottom: 2rem;
    text-align: justify;
  }

  #paragraph-four {
    margin-bottom: 2rem;
    text-align: justify;
  }

  #paragraph-five {
    margin-bottom: 2rem;
    text-align: justify;
  }

  #paragraph-six {
    margin-bottom: 2rem;
    text-align: justify;
  }

  #paragraph-seven {
    margin-bottom: 2rem;
    text-align: justify;

    #tax-administrator-requisites-one {
      margin-bottom: 2rem;
    }

    #tax-administrator-requisites-two {
      #row-one {
        display: flex;
        justify-content: space-between;
        text-align: center;
      }

      #row-two {
        display: flex;
        justify-content: space-between;
        text-align: center;
      }
    }
  }

  #paragraph-eight {
    #tax-payer-name-two {
      width: 15rem;
      margin-top: 0.75rem;
    }

    #tax-payer-code-two {
      width: 15rem;
      margin-bottom: 0.75rem;
    }

    #location-two {
      width: 30rem;
    }

    #tax-payer-requisites-final {
      #tax-payer-requisites-final-row-1 {
        display: flex;
        justify-content: space-between;
        margin-top: 1.5rem;

        #tax-payer-representative-name-two {
          width: 15rem;
        }
      }

      #tax-payer-requisites-final-row-2 {
        display: flex;
        justify-content: space-between;
        margin-top: 1.5rem;
      }
    }
  }
}
</style>
