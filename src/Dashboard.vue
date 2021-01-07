<template>
  <div id="dashboard">
    <!-- Navigation -->
    <nav id="dashboard-nav">
      <div id="dashboard-nav-content">
        <router-link id="dashboard-back-button" class="emphasised-text" to="/"><i class="far fa-arrow-alt-circle-left"></i> {{ strings[lang]["navBack"] }}</router-link>  
        <a href="#" v-if="this.$store.getters.isLoggedIn" id="dashboard-logout-button" class="emphasised-text" @click="logOut"><i class="fas fa-sign-out-alt"></i> {{ strings[lang]["navLogOut"] }}</a>
      </div>
    </nav>
    <!-- Welcome back div -->
    <div id="header-div">
      <h1 v-if="reportSent" class="emphasised-text-alt">Report sent successfully!</h1>
      <h1 v-else>{{ strings[lang]["headWelcome"] }}, <span class="emphasised-text-gradient">{{ parsedName }}</span>!</h1>
    </div>
    <!-- Reports block -->
    <div id="reports-div" class="">
      <div id="reports-nav">
        <div id="filter-box">
          <i class="fas fa-search emphasised-text"></i>
          <input type="text" name="filter-docs" id="filter-docs" placeholder="What are you working on today?" v-model="userInput">
        </div>
      </div>
      <div id="reports" class="">
        <carousel :perPage="3" :navigationEnabled="true" paginationActiveColor="#ffd700" paginationColor="#f5f5f5">
          <slide class="report animated fadeIn" :key="item.id" v-if="item.name.toLowerCase().includes(searchString)" v-for="item in currentUserReports" :style=" {backgroundImage: 'url(' + item.thumbUrl + ')' } ">
            <!-- <img :src="item.thumbUrl" :alt="item.name"> -->
            <div class="hover-overlay">
              <div class="description">
                <h3><span>{{ item.name }}</span></h3>
                <p>{{ item.description }}</p>
                <router-link v-if="item.ready" :to="'/' + item.component">
                  <input type="button" :value="strings[lang]['reportsChoose']" class="report-btn">
                </router-link>
                <div v-else>
                  <input type="button" :value="strings[lang]['reportsWip']" class="report-btn-wip" disabled="disabled">
                </div>
              </div>
            </div>
          </slide>
        </carousel>
      </div>
    </div>
    <!-- Add Report and Help Section  -->
    <section id="add-report-help-div">
      <div id="add-report">
        <i class="fas fa-shopping-bag fa-3x" @click="shopTemplates"></i>
        <span>{{ strings[lang]['getTemplates'] }}</span>
      </div>
      <div id="help">
        <i class="fas fa-question fa-3x" @click="getHelp"></i>
        <span>{{ strings[lang]['help'] }}</span>
      </div>
    </section>

    <div id="add-templates-div" @click.self="closeShopTemplates">
      <div id="add-template-box">
        <div id="close-btn-div">
          <i class="fas fa-times" @click="closeShopTemplates"></i>
        </div>
        <div id="add-template-box-content">
          <h3 class="emphasised-text-gradient">{{ strings[lang]['reportsWip'] }}</h3>
        </div>
      </div>
    </div>
    <div id="get-help-div" @click.self="closeGetHelp">
        <div id="get-help-box">
          <div id="close-btn-div">
            <i class="fas fa-times" @click="closeGetHelp"></i>
          </div>
          <div id="get-help-box-content">
            <h3 class="emphasised-text-gradient">{{ strings[lang]['reportsWip'] }}</h3>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { Carousel, Slide } from 'vue-carousel'
  import firebase from 'firebase'

  export default {
    name: 'dashboard',
    data() { 
      return {
        userInput: "",
        strings: {
          "lt": {
            "navBack": "Atgal į Pradinį",
            "navLogOut": "Atsijungti",
            "headWelcome": "Sveikas sugrįžęs",
            "reportsChoose": "Pasirinkti",
            "reportsWip": "Ruošiama",
            "getTemplates": "Pridėti šablonų",
            "help": "Pagalba"
          },
          "en": {
            "navBack": "Back to Main",
            "navLogOut": "Log Out",
            "headWelcome": "Welcome back",
            "reportsChoose": "Choose",
            "reportsWip": "Work in Progress",
            "getTemplates": "Get templates",
            "help": "Ask for help"
          }
        }
      }
    },
    computed: {
      greeting() {
        if (this.reportSent) {
          return 'Report sent successfully!'
        } else {
          return 'Welcome back, ' + this.parsedName
        }
      },
      reportSent() {
        return this.$store.getters.getReportSent
      },
      lang() {
        return this.$store.getters.getLang
      },
      currentUserReports() {
        return this.$store.getters.getCurrentUserReports
      },
      searchString() {
        return this.userInput.toLowerCase()
      },
      parsedName() {
        let currUserName = this.$store.getters.getCurrentUser
        let currNameSplit = currUserName.split('@')[0]
        let currNameTitle = currNameSplit.charAt(0).toUpperCase() + currNameSplit.substring(1);

        return currNameTitle
      }
    },
    methods: {
      shopTemplates() {
        $("#add-templates-div").removeClass('animated fadeOut faster')
        $("#add-template-box").removeClass('animated fadeOut faster')
        $("#add-templates-div").addClass('animated fadeIn faster')
        $("#add-template-box").addClass('animated fadeIn faster')
        $("#add-templates-div").css('visibility', 'visible')
        },
      closeShopTemplates() {
        $("#add-templates-div").removeClass('animated fadeIn faster')
        $("#add-template-box").removeClass('animated fadeIn faster')
        $("#add-template-box").addClass('animated fadeOut faster')
        $("#add-templates-div").addClass('animated fadeOut faster')

        setTimeout(() => {
          $("#add-templates-div").css('visibility', 'hidden')
        }, 500)
      },
      getHelp() {
        $("#get-help-div").removeClass('animated fadeOut faster')
        $("#get-help-box").removeClass('animated fadeOut faster')
        $("#get-help-div").addClass('animated fadeIn faster')
        $("#get-help-box").addClass('animated fadeIn faster')
        $("#get-help-div").css('visibility', 'visible')
        },
      closeGetHelp() {
        $("#get-help-div").removeClass('animated fadeIn faster')
        $("#get-help-box").removeClass('animated fadeIn faster')
        $("#get-help-box").addClass('animated fadeOut faster')
        $("#get-help-div").addClass('animated fadeOut faster')

        setTimeout(() => {
          $("#get-help-div").css('visibility', 'hidden')
        }, 500)
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
    beforeCreate() {
      // Fetch reports from the store:
      this.$store.commit('fetchReports');
    },
    mounted() {
      // Animations:
      
      // Declare variables:
      const headerDiv = document.getElementById('header-div');
      const reportsDiv = document.getElementById('reports-div');
      const addHelpDiv = document.getElementById('add-report-help-div');
        
      // Add animations:
      headerDiv.classList.add('animated', 'fadeIn');
      reportsDiv.classList.add('animated', 'delay-1s', 'fadeIn')
      addHelpDiv.classList.add('animated', 'delay-1s', 'fadeIn')

      },
      components: {
        Carousel,
        Slide
      }
    }
</script>

<style lang="scss">
  @import url('https://fonts.googleapis.com/css?family=Montserrat&display=swap');


  $main-font: 'Montserrat', sans-serif;
  $black-text-color: #133337;
  $black-text-color-alt: #2c4c50;
  $black-text-color-alt-2: #242F3E;
  $white-text-color: #f5f5f5;
  $emphasis-color: #ffd700;
  $emphasis-color-alt: #ffa500;

  /* Document */

  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  html, body {
    background: $black-text-color-alt;
    color: $white-text-color;
    font-family: $main-font;
    // scroll-behavior: smooth;

    a {
      text-decoration: none;
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
  }


  /* Navigation */
  
  #dashboard-nav {
    height: 5vh;

    #dashboard-nav-content {
      width: 100%;
      height: 100%;
      max-width: 1800px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0 3rem;

      a {
        color: $emphasis-color;
        transition: color 0.2s;
        display: block;

        &:hover {
          color: $emphasis-color-alt !important;
        }
      }
    }
  }

  // #dashboard-nav a

  /* Welcome Back Div */
  #header-div {
    height: 7vh;
    
    h1 {
      font-weight: normal;
      text-align: center;
      font-size: 1.2rem;
      opacity: 1;
      transition: opacity .3s; 
    }
  }

  /* Content */
  
  #reports-div {
    background: lighten($black-text-color-alt-2, 1%);
    border: solid 5px transparent;
    height: 75vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 2rem;
  }

  /* Documents */

  #reports-div {
    #reports-nav {
      height: 2rem;

      #filter-box {
        text-align: right;
        height: 2rem;

        input {
          width: 25%;
          height: 100%;
          border: 0.1rem solid #f5f5f5;
          border-radius: 1rem;
          padding: 0 1rem;
          margin-left: 0.5rem;
          font-family: $main-font; 
          font-size: 1rem;
          background: $white-text-color;
          transition: border 0.3s;

          &:focus {
            outline: none;
          }

          &:hover {
            border: 0.1rem solid $emphasis-color;
            transition: border 0.3s;
          }
        }
      }
    }

    #reports {
      margin-top: 2rem;

      .report {
        margin-right: 2rem;
        background-position: top;
        background-repeat: no-repeat;
        background-size: cover;
        height: 50vh;

        .hover-overlay {
          opacity: 0;
          background: linear-gradient(to bottom, $emphasis-color, $emphasis-color-alt);
          color:#f5f5f5;
          height: 100%;
          text-align: center;
          display: flex;
          align-items: center;
          transition: opacity 0.3s;

          &:hover {
            opacity: 1;
            transition: opacity 0.3s;
          }
          
          .description {
            padding: 3rem;
            display: flex;
            height: 100%;
            flex-direction: column;
            justify-content: space-around;
            
            h3 {
              color: $black-text-color;
              font-weight: bold;
              font-size: 1.25rem;
            }

            p {
              color: $black-text-color;
              text-align: justify;
            }

            .report-btn {
              display: block;
              border: none;
              background: #008000;
              color: $white-text-color;
              font-family: $main-font;
              width: 8rem;
              margin: 0 auto;
              text-align: center;
              padding: 0.8rem;
              font-size: 1.1rem;
              transition-property: background, color;
              transition-duration: 0.2s;
              cursor: pointer;
              border-radius: 5px;
            }

            .report-btn:hover {
              background: #065535;
              color: $white-text-color;
              transition-property: background, color;
              transition-duration: 0.2s;
            }

            .report-btn-wip {
              display: block;
              border: none;
              background: #065535;
              color: $white-text-color;
              font-family: $main-font;
              width: 12rem;
              margin: 0 auto;
              text-align: center;
              padding: 0.8rem;
              font-size: 1.1rem;
              transition-property: background, color;
              transition-duration: 0.2s;
              border-radius: 5px;
            }
          }
        }
      }

      .VueCarousel-navigation {

        .VueCarousel-navigation-button {
          color: $emphasis-color;
          visibility: visible !important;
        }
      }
    }
  }

  /* Add report and help */

  #add-report-help-div {
    display: flex;
    justify-content: center;
    height: 13vh;
    
    div {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: 0 2rem;
    }

    i {
      font-size: 2rem;
      display: block;
      width: 4rem;
      height: 4rem;
      line-height: 4rem;
      text-align: center;
      color: $emphasis-color;
      border-radius: 50%;
      margin-bottom: 0.25rem;
      cursor: pointer;
      transition-property: background, color;
      transition-duration: 0.2s;

      &:hover {
        background: $emphasis-color-alt;
        color: $white-text-color;
        transition-property: background, color;
        transition-duration: 0.2s;
      }
    }
  }

  #add-templates-div {
    position: absolute;
    top: 0;
    left: 0;
    background: rgba(0, 0, 0, .6);
    width: 100%;
    height: 100%;
    z-index: 999;
    visibility: hidden;
    display: flex;
    align-items: center;
    justify-content: center;

    #add-template-box {
      position: relative;
      width: 75rem;
      height: 45rem;
      background: $white-text-color;

      #close-btn-div {
        color: $black-text-color;
        width: 100%;
        height: 3rem;
        padding: 0 1rem;
        text-align: right;
        line-height: 3rem;

        i {
          cursor: pointer;
          color: $black-text-color;
          transition: color .3s;
          font-size: 1.5rem;

          &:hover {
            color: $emphasis-color-alt;
            transition: color .3s;
          }
        }
      }

      #add-template-box-content {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
        height: 100%;
        padding: 0 3rem;
        color: $black-text-color;

        h3 {
          font-size: 2.5rem;
        }
      }
    }
  }

  #get-help-div {
    position: absolute;
    top: 0;
    left: 0;
    background: rgba(0, 0, 0, .6);
    width: 100%;
    height: 100%;
    z-index: 999;
    visibility: hidden;
    display: flex;
    align-items: center;
    justify-content: center;

    #get-help-box {
      position: relative;
      width: 75rem;
      height: 45rem;
      background: $white-text-color;

      #close-btn-div {
        color: $black-text-color;
        width: 100%;
        height: 3rem;
        padding: 0 1rem;
        text-align: right;
        line-height: 3rem;

        i {
          cursor: pointer;
          color: $black-text-color;
          transition: color .3s;
          font-size: 1.5rem;

          &:hover {
            color: $emphasis-color-alt;
            transition: color .3s;
          }
        }
      }

      #get-help-box-content {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
        height: 100%;
        padding: 0 3rem;
        color: $black-text-color;

        h3 {
          font-size: 2.5rem;
        }
      }
    }
  }






</style>
