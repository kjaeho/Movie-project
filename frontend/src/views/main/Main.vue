<template>
  <div>
    <div style="width:100% !important; height:47rem; background-image:url(https://3v14en34n4qsadzlwpatrq14-wpengine.netdna-ssl.com/wp-content/uploads/2017/03/woodland_wanderer_dribbble.gif); background-repeat:no-repeat; background-size:100% 100%">
      <div class="d-flex justify-content-center align-items-center" style="height:100%;">
        <div class="form-group d-flex justify-content-center row" style="width:100%">
          <span class="col-12 d-flex justify-content-center pb-2" style="color:white; font-family: 'Black Han Sans', sans-serif; font-size:3rem; opacity:0.8;">팝콘 🅰🅽🅶🅻🅴</span>
          <i class="fas fa-search my-auto mr-2" style="font-size:3rem; color:lightgray; opacity:0.8;"></i>
          <input @keypress.enter="Search(search)" v-model="search" class="form-control" style="width:25rem; height:3rem; opacity:0.7; border-radius:15px;">
        </div>
      </div>
    </div>

    <div class="container col-md-10 mt-5">
      <span class="" style="color:white; font-size:2rem; font-family: 'Black Han Sans', sans-serif;">오늘의 영화</span>
      <svg id="color" class="mr-2" style="margin-left:72%" enable-background="new 0 0 24 24" height="35" viewBox="0 0 24 24" width="35" xmlns="http://www.w3.org/2000/svg"><g><g><path d="m21.772 14h-20.022c-.414 0-.75-.336-.75-.75v-12.5c0-.414.336-.75.75-.75h20.022c.487 0 .919.273 1.129.713.209.439.147.947-.159 1.325l-4.026 4.962 4.026 4.962c.307.377.368.885.159 1.325-.21.44-.641.713-1.129.713zm-.194-1.092h.01z" fill="#2196f3"/></g></g><g><g><path d="m13.25 10h-.5c-.965 0-1.75-.785-1.75-1.75v-2.5c0-.965.785-1.75 1.75-1.75h.5c.965 0 1.75.785 1.75 1.75v2.5c0 .965-.785 1.75-1.75 1.75zm-.5-4.5c-.138 0-.25.112-.25.25v2.5c0 .138.112.25.25.25h.5c.138 0 .25-.112.25-.25v-2.5c0-.138-.112-.25-.25-.25z" fill="#fafafa"/></g></g><g><g><path d="m8.25 10h-1.5c-.965 0-1.75-.785-1.75-1.75v-2.5c0-.965.785-1.75 1.75-1.75h1.5c.414 0 .75.336.75.75s-.336.75-.75.75h-1.5c-.138 0-.25.112-.25.25v2.5c0 .138.112.25.25.25h.75v-.5c-.414 0-.75-.336-.75-.75s.336-.75.75-.75h.75c.414 0 .75.336.75.75v2c0 .414-.336.75-.75.75z" fill="#fafafa"/></g></g><g><g><path d="m1.75 24c-.414 0-.75-.336-.75-.75v-22.5c0-.414.336-.75.75-.75s.75.336.75.75v22.5c0 .414-.336.75-.75.75z" fill="#607d8b"/></g></g><g><g><path d="m6.75 10c-.965 0-1.75-.785-1.75-1.75v-2.5c0-.965.785-1.75 1.75-1.75h1.5c.414 0 .75.336.75.75s-.336.75-.75.75h-1.5c-.138 0-.25.112-.25.25v2.5c0 .138.112.25.25.25h.75v-.5c-.414 0-.75-.336-.75-.75s.336-.75.75-.75h.75c.414 0 .75.336.75.75v2c0 .414-.336.75-.75.75zm5.25-10h-10.25c.414 0 .75.336.75.75v13.25h9.5v-4.169c-.591-.281-1-.884-1-1.581v-2.5c0-.697.409-1.3 1-1.581z" fill="#1d83d4"/></g></g><g><g><path d="m1.75 0c-.414 0-.75.336-.75.75v22.5c0 .414.336.75.75.75z" fill="#546d79"/></g></g><g><g><path d="m15 7h-1.5v1.25c0 .138-.112.25-.25.25h-.5c-.138 0-.25-.112-.25-.25v-1.25h-1.5v1.25c0 .965.785 1.75 1.75 1.75h.5c.965 0 1.75-.785 1.75-1.75z" fill="#dadada"/></g></g><g><g><path d="m8.957 7h-2.164c-.028.078-.043.162-.043.25 0 .414.336.75.75.75v.5h-.75c-.138 0-.25-.112-.25-.25v-1.25h-1.5v1.25c0 .965.785 1.75 1.75 1.75h1.5c.414 0 .75-.336.75-.75v-2c0-.088-.015-.172-.043-.25z" fill="#dadada"/></g></g></svg>
      <span @click="goRecommend" style="color:white; font-size:1rem; font-family: 'Black Han Sans', sans-serif; cursor:pointer;">추천 받으러 가기</span>
      <div>
        <div v-for="movie in todayMovie" :key="movie.id" class="card m-4 text-white imgHoverEvent event2" style="width:12rem; display:inline-block; border:none; border-radius:10px;">
          <div class="imgBox"><img v-if="movie.poster" :src="movie.poster" class="card-img-top" style="height:17rem"></div>
          <div class="imgBox"><img v-if="!movie.poster" src="../../assets/img/noimg.png" class="card-img-top" style="height:17rem"></div>
          <div class="card-img-overlay hoverBox">
            <span class="movie-text">
              <p class="card-title p1" style="font-size:1.5rem; color:crimson; font-weight:bold; margin-top:50%">{{movie.title}}</p>
              <div class="d-flex justify-content-center">
                <button @click="goDetail(movie.movie_id)" class="btn btn-defualt" style="border:1px red solid; border-radius:10px"><span style="font-weight:bold; color:white;">view</span></button>
              </div>
            </span>
          </div>
        </div>
      </div>
    </div>
    
    <div class="container col-md-10 mt-5">
      <span class="" style="color:white; font-size:2rem; font-family: 'Black Han Sans', sans-serif;">팝콘 ANGLE 회원이 선택한 영화</span>
      <svg id="flat" class="mr-2" style="margin-left:51%;" height="35" viewBox="0 0 512 512" width="35" xmlns="http://www.w3.org/2000/svg"><path d="m48 320v-104h-24v-48a32 32 0 0 1 32-32h160a32 32 0 0 1 32 32v40h-24v112z" fill="#548aff"/><path d="m248 200v31.53a48.46108 48.46108 0 0 1 -76.64 39.44l-32.75-23.38989-26.61-19.01v-28.57011h32l16.27 6.97 39.73 17.03v-24z" fill="#ffceb6"/><path d="m160.27 206.97-21.66 40.61-26.61-19.01v-28.57h32z" fill="#ffbfa1"/><path d="m152 88v48a23.59674 23.59674 0 0 1 -1.37988 8 23.99641 23.99641 0 0 1 -46.62012-8v-48z" fill="#ffb089"/><rect fill="#4976f2" height="32" rx="8" width="16" x="64" y="176"/><path d="m168 128v32l-49.88 93.53a50.00436 50.00436 0 0 1 -94.12-23.53v-22h48v16l56-64v-48h24z" fill="#ffceb6"/><rect fill="#4976f2" height="24" rx="8" width="16" x="192" y="176"/><path d="m336 184h24v16h-24z" fill="#d1e4ff"/><path d="m376 184h104v16h-104z" fill="#d1e4ff"/><path d="m312 216h88v16h-88z" fill="#d1e4ff"/><path d="m416 216h80v16h-80z" fill="#d1e4ff"/><path d="m320 104h-48a8.00008 8.00008 0 0 1 -8-8v-48a8.00008 8.00008 0 0 1 8-8h24v16h-16v32h32v-40h16v48a8.00008 8.00008 0 0 1 -8 8z" fill="#d1e4ff"/><path d="m278.059 48h67.882v16h-67.882z" fill="#ef5e3b" transform="matrix(.707 -.707 .707 .707 51.777 237.008)"/><g fill="#d1e4ff"><path d="m336 400h24v16h-24z"/><path d="m456 400h24v16h-24z"/><path d="m376 400h64v16h-64z"/><path d="m344 432h56v16h-56z"/><path d="m312 432h16v16h-16z"/><path d="m416 432h80v16h-80z"/><path d="m320 320h-48a8.00008 8.00008 0 0 1 -8-8v-48a8.00008 8.00008 0 0 1 8-8h24v16h-16v32h32v-40h16v48a8.00008 8.00008 0 0 1 -8 8z"/></g><path d="m278.059 264h67.882v16h-67.882z" fill="#ef5e3b" transform="matrix(.707 -.707 .707 .707 -100.952 300.266)"/><path d="m352 272h112v88h-112z" fill="#548aff"/><path d="m464 296v64h-112v-32l24.06006-14.43994a27.64191 27.64191 0 0 1 30.80994 1.58984 27.62141 27.62141 0 0 0 33.85-.52978z" fill="#4976f2"/><path d="m168 128v3.12988a46.05736 46.05736 0 0 1 -32 12.87012h-8v-32h24z" fill="#ffbfa1"/><path d="m136 128a32 32 0 0 1 -32-32v-16l24-24h40v40a32 32 0 0 1 -32 32z" fill="#ffceb6"/><path d="m168 56 7.80063-3.90031a14.8328 14.8328 0 0 0 8.19937-13.26687 14.8328 14.8328 0 0 0 -14.8328-14.83282h-33.1672a32 32 0 0 0 -32 32v24l24-24z" fill="#c47220"/><path d="m48 496v-176h176v176h-72l-16-104-24 104z" fill="#718799"/><path d="m408 160 48-32v-56l-48-32-48 32v56z" fill="#ffb401"/><path d="m456 72-48 32-48-32 48-32z" fill="#ffd873"/><path d="m408 160v-56l48-32v56z" fill="#ffc431"/></svg>
      <span @click="goMovie" style="color:white; font-size:1rem; font-family: 'Black Han Sans', sans-serif; cursor:pointer;">영화 골라보기</span>
      <div>
        <div v-for="movie in choiceMovie" :key="movie.id" class="card m-4 text-white imgHoverEvent event2" style="width:12rem; display:inline-block; border:none; border-radius:10px;">
          <div class="imgBox"><img v-if="movie.poster" :src="movie.poster" class="card-img-top" style="height:17rem"></div>
          <div class="imgBox"><img v-if="!movie.poster" src="../../assets/img/noimg.png" class="card-img-top" style="height:17rem"></div>
          <div class="card-img-overlay hoverBox">
            <span class="movie-text">
              <p class="card-title p1" style="font-size:1.5rem; color:crimson; font-weight:bold; margin-top:50%">{{movie.title}}</p>
              <div class="d-flex justify-content-center">
                <button @click="goDetail(movie.movie_id)" class="btn btn-defualt" style="border:1px red solid; border-radius:10px"><span style="font-weight:bold; color:white;">view</span></button>
              </div>
            </span>
          </div>
        </div>
      </div>
    </div>

    <div class="container col-md-10 mt-5">
      <span class="" style="color:white; font-size:2rem; font-family: 'Black Han Sans', sans-serif;">천만이 선택한 영화</span>
      <svg class="mr-2" style="margin-left:64%;" id="Capa_1" enable-background="new 0 0 512 512" height="35" viewBox="0 0 512 512" width="35" xmlns="http://www.w3.org/2000/svg"><g><path d="m497.08 512h-131.87l-109.208-29-109.212 29h-131.87c-9.39 0-17.01-8.84-14.4-18.6l29.4-118.2 226.23-32 225.93 32 29.4 118.2c2.61 9.76-5 18.6-14.4 18.6z" fill="#fff5f5"/><path d="m497.08 512c9.4 0 17.01-8.84 14.4-18.6l-29.4-118.2-225.93-32-.148.021v139.779l109.208 29z" fill="#efe2dd"/><path d="m482.084 135v240.2h-452.166v-240.2c0-8.401 6.599-15 15-15h91.083c8.401 0 15 6.599 15 15 0 36.899 18.9 70.499 51 89.7 22.2 13.5 40.8 32.1 54 54.3 12.9-21.899 31.5-40.8 54-54.3 32.1-19.2 51-52.8 51-89.7 0-8.401 6.599-15 15-15h91.083c8.401 0 15 6.599 15 15z" fill="#474f54"/><path d="m482.084 375.2v-240.2c0-8.401-6.599-15-15-15h-91.083c-8.401 0-15 6.599-15 15 0 36.899-18.9 70.499-51 89.7-22.5 13.5-41.1 32.401-54 54.3v96.2z" fill="#32393f"/><g><path d="m256.089 329.766c-6.46 0-12.275-3.896-14.312-10.02-9.697-29.048-29.414-53.672-55.576-69.448-40.826-24.639-65.2-67.734-65.2-115.298 0-74.443 60.557-135 135-135s135 60.557 135 135c0 47.651-24.448 90.791-65.391 115.4-26.03 15.645-45.645 40.107-55.21 68.877-2.05 6.123-7.866 10.489-14.311 10.489z" fill="#fed843"/></g><path d="m256.089 329.766c6.445 0 12.261-4.365 14.312-10.488 9.565-28.77 29.18-53.232 55.21-68.877 40.942-24.609 65.391-67.749 65.391-115.4 0-74.443-60.557-135-135-135v329.738c.032-.001.054.027.087.027z" fill="#fabe2c"/><g><path d="m301.001 105c0 18.9-12.001 36-29.7 42.299 0 8.401-6.899 16.5-15.3 16.5-8.101 0-15-5.4-15-13.799 0-12.601 5.7-23.101 15-28.5 1.5-.901 3.3-1.8 5.099-2.401 6-2.1 9.901-7.8 9.901-14.099 0-8.401-6.599-15-15-15s-15 6.599-15 15c0 8.399-6.599 15-15 15s-15-6.601-15-15c0-24.901 20.099-45 45-45s45 20.099 45 45z" fill="#474f54"/></g><g><circle cx="256.001" cy="195" fill="#474f54" r="15"/></g><g fill="#32393f"><path d="m271.001 195c0-8.286-6.716-15-15-15v30c8.284 0 15-6.716 15-15z"/><path d="m301.001 105c0 18.9-12.001 36-29.7 42.299 0 8.401-6.899 16.5-15.3 16.5v-42.299c1.5-.901 3.3-1.8 5.099-2.401 6-2.1 9.901-7.8 9.901-14.099 0-8.401-6.599-15-15-15v-30c24.901 0 45 20.099 45 45z"/></g></g><g><path d="m345.551 433.36c-1.67-6.68-7.67-11.36-14.55-11.36h-150c-6.88 0-12.88 4.68-14.55 11.36l-19.66 78.64h218.42z" fill="#efe2dd"/></g><path d="m256.001 512h109.21l-19.66-78.64c-1.67-6.68-7.67-11.36-14.55-11.36h-75z" fill="#e1d3ce"/></svg>
      <span @click="goRecommend" style="color:white; font-size:1rem; font-family: 'Black Han Sans', sans-serif; cursor:pointer;">다음 천만 영화는?</span>
      <div>
        <div v-for="movie in tenmillionMovie" :key="movie.id" class="card m-4 text-white imgHoverEvent event2" style="width:12rem; display:inline-block; border:none; border-radius:10px;">
          <div class="imgBox"><img v-if="movie.poster" :src="movie.poster" class="card-img-top" style="height:17rem"></div>
          <div class="imgBox"><img v-if="!movie.poster" src="../../assets/img/noimg.png" class="card-img-top" style="height:17rem"></div>
          <div class="card-img-overlay hoverBox">
            <span class="movie-text">
              <p class="card-title p1" style="font-size:1.5rem; color:crimson; font-weight:bold; margin-top:50%">{{movie.title}}</p>
              <div class="d-flex justify-content-center">
                <button @click="goDetail(movie.movie_id)" class="btn btn-defualt" style="border:1px red solid; border-radius:10px"><span style="font-weight:bold; color:white;">view</span></button>
              </div>
            </span>
          </div>
        </div>
      </div>
    </div>
    

  </div>
</template>

<script>
import axios from 'axios'
import constants from '../../lib/constants';

export default {
  data() {
    return {
      search: "",
      todayMovie: [],
      choiceMovie: [],
      tenmillionMovie:[],
    }
  },
  methods: {
    callTen() {
      axios.get(`${constants.SERVER_URL}/movies/tenmillion`)
        .then((res) => {
          this.tenmillionMovie = res.data
        })
    },
    callToday() {
      axios.get(`${constants.SERVER_URL}/movies/today/movie`)
        .then((res) => {
          this.callPopcorn()
          this.callTen()
          this.todayMovie = res.data.random
        })
    },
    callPopcorn() {
      axios.get(`${constants.SERVER_URL}/movies/today/movie`)
        .then((res) => {
          this.choiceMovie = res.data.best
        })
    },
    goDetail(id) {
        this.$router.push(`/movie/${id}`).catch(() => {
            this.$router.go()          
        })
    },
    goRecommend() {
      this.$router.push('/movierecommend').catch(() => {
        this.$router.go()
      })
    },
    goMovie() {
      this.$router.push('/movie').catch(() => {
        this.$router.go()
      })
    },
    Search(data) {
      this.$cookies.set('searchKeyword',data)
      this.$router.push('/searchmovie').catch(() => {
        this.$router.go()
      })
    },
  },
  created() {
    this.callToday()
  },
}
</script>

<style>

</style>