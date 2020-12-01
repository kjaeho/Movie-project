<template>
  <div class="app" style="background-color:black">
    <Header :isHeader="isHeader"/>
    <router-view/>
    <LoginModal />
    <JoinModal />
  </div>
</template>

<script> 
import Header from '@/components/Header'
import constants from '@/lib/constants'
import LoginModal from './components/login/LoginModal.vue'
import JoinModal from './components/join/JoinModal.vue'

export default {
  name: 'App',
  components: { 
    Header,
    LoginModal,
    JoinModal,
  },
  created() {
      let url = this.$route.name;
  
      this.checkUrl(url);

      console.log('App.vue')
    let token = window.$cookies.get('FootballDiary')
    if (token) {
      this.$store.commit('setToken', token)
      console.log('App.vue.afterSetToken')
      this.$store.dispatch('getUserFromServer')
    } else {
      // this.onLogout()
  }
  },
  watch: {
      $route (to){
          this.checkUrl(to.name);
      }
  },
  methods : {
      checkUrl(url) { 

          let array = [
              constants.URL_TYPE.USER.LOGIN,
              constants.URL_TYPE.USER.JOIN,
          ];

          let isHeader = true;
          array.map(path => {
              if (url === path)
                  isHeader = false;
          })
          this.isHeader = isHeader;

      },
  },
  data: function () {
        return {
            isHeader: true,
            constants
        } 
    }
}
</script>

<style>
.app {
  /* background-color: rgb(53, 52, 52); */
}
</style>
