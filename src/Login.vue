<template>
  <div id="login">
    <div id="nav">
      <div id="nav-content">
        <router-link id="back-button" class="emphasised-text" to="/"><i class="far fa-arrow-alt-circle-left"></i> {{ strings[lang]['navBack'] }}</router-link>  
      </div>
    </div>
      
    <div id="login-div">
      <div id="login-block">  
        <div id="login-logo-div">
          <div id="login-logo-main">
            <img id="logo-login" src="./assets/logo-colored-alt.png" alt="logo">
            <p id="logo-text"><span class="emphasised-text"> Robo</span>dokas</p>
          </div>
          <p>{{ strings[lang]['mainText'] }}</p>
        </div>

        <div id="form-div">
          <form action="#" @submit.prevent="">
            <label for="login-email">{{ strings[lang]['formEmail'] }}:</label>
            <input type="text" name="login-email" id="login-email" v-model="userEmail">
            <label for="login-email">{{ strings[lang]['formPwd'] }}:</label>
            <input type="password" name="login-password" id="login-password" v-model="userPassword" autocomplete="on">
            <input type="submit" class="contact-btn" :value="strings[lang]['formLogIn']" @click="logIn">
          </form>
        </div>
      </div>
    </div>
  </div>   
</template>

<script>
import firebase from 'firebase'

export default {
  name: 'login',
  data() { 
    return {
      userEmail: '',
      userPassword: '',
      strings: {
        "lt": {
          "navBack": "Atgal į Pradinį",
          "mainText": "Prisijungimas prie Vartotojų zonos: ",
          "formEmail": "Elektroninis paštas",
          "formPwd": "Slaptažodis",
          "formLogIn": "Prisijungti"
        },
        "en": {
          "navBack": "Back to Main",
          "mainText": "Login to User Zone: ",
          "formEmail": "Email address:",
          "formPwd": "Password",
          "formLogIn": "Log In"
        }
      }
    }
  },
  computed: {
    lang() {
      return this.$store.getters.getLang
    }
  },
  methods: {
    logIn() {
      firebase
        .auth()
        .signInWithEmailAndPassword(this.userEmail, this.userPassword)
        .then(
          user => {
            this.$store.commit('logIn', user)
            this.$router.push('/dashboard');
            },
          err => {
            alert(err.message);
          })
    }
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
    background: $black-text-color-alt !important;
    color: $white-text-color;
    font-family: $main-font;

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

    #nav {
      height: 5vh;

      #nav-content {
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        max-width: 1800px;
        padding: 0 3rem;

        #back-button {
          color: $emphasis-color !important;
          transition: color .3s;

          &:hover {
            color: $emphasis-color-alt !important;
            transition: color .3s;  
          }
        }
      }
    }
    
    #login-div {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 95vh;

      #login-block {  
        background: lighten($black-text-color-alt, 1%);
        border: solid 5px transparent;
        box-shadow:
          -3px -3px 13px 3px lighten($black-text-color-alt, 4%),
          4px 4px 15px 6px darken($black-text-color-alt, 9%);

        // background: $black-text-color;
        color: #f5f5f5;
        width: 25vw;
        height: 75vh;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 3rem;

        #login-logo-div {
          flex: 1;
          display: flex;
          flex-direction: column;
          justify-content: space-between;
          
          #login-logo-main {
            display: flex;
            align-items: center;
            justify-content: center;

            #logo-login {
              width: 4rem;
            }

            #logo-text {
              font-size: 2rem;
            }
          }

          p {
            text-align: center;
            font-weight: bold;
            font-size: 1.05rem;  
          }
        }

        #form-div {
          flex: 2;
          display: flex;
          align-items: center;
          justify-content: center;

          form {
            width: 100%;
            display: flex;
            flex-direction: column;
          
            label {
              font-size: .95rem;
              margin-bottom: 0.6rem;
            }

            input[type=text], input[type=password] {
              height: 2.3rem;
              font-family: $main-font;
              padding: 0.5rem;
              font-size: 1.1rem;
              line-height: 2rem;
              background: $white-text-color;
              border: none;
              border-radius: 5px;
              margin-bottom: 1rem;
            }

            input[type=submit] {
              margin-top: 2rem;
              border-radius: 5px;
            }

            .contact-btn {
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

              &:hover {
                background: $emphasis-color-alt;
                color:$white-text-color;
                transition-property: background, color;
                transition-duration: 0.2s;
              }
            }
          }
        }
      }
    }
  }
  




</style>