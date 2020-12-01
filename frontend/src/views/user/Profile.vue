<template>
  <div class="container col-md-10 pt-5">
    <div class="profile">
      <div class="col-sm-12">
        <div class="card p-4 bg-transparent border-light">
          <div class="row">
            <div v-if="profileData.profile_image" class="text-center my-auto col-12 col-md-2">
              <img style="border-radius:50%;width:90%;" :src="profileData.profile_image" alt="...">
            </div>
            <div v-else class="text-center my-auto col-12 col-md-2">
              <img style="border-radius:50%;width:90%;" src="https://placekitten.com/300/300" alt="...">
            </div>
            <div class="col-12 col-md-6 my-4 mx-auto">
              <p class="mb-0 text-light">닉네임: {{ profileData.username}}</p>
              <p class="mb-0 text-light">이메일: {{ profileData.email}}</p>
              <p class="mb-0 text-light">평가한 영화: {{ ratedMovieCnt }}개</p>
              <p class="mb-0 text-light">찜한 영화: {{ likedMovieCnt }}개</p>
            </div>
            <div class="ml-auto text-right">
              <b-button data-toggle="modal" data-target="#Update" size="sm" variant="transparent" class="text-light border-light mr-2">수정</b-button>
              <b-button size="sm" class="text-light mr-2 border-light" variant="transparent" @click="logout">로그아웃</b-button>
            </div>
          </div>
        </div>
      </div>
      <div class="mt-5">
        <div class="col-md-12">
          <div class="category">
            <b-tabs content-class="mb-4" style="white-space:nowrap; font-weight:bold;" justified active-nav-item-class="font-weight-bold text-uppercase text-danger">
              <b-tab title="평가 한 영화" title-item-class="tab-title-class" active>
                <div class="row">
                  <div class="card text-white col-12 col-sm-6 col-md-4 col-lg-3 p-4 imgHoverEvent event2" style="border:none; background-color:black" v-for="movie in ratedMovieData" :key="movie.id">
                    <div class="imgBox"><img v-if="movie.poster" :src="movie.poster" class="card-img img-img" style="width:100%"></div>
                    <div class="imgBox"><img v-if="!movie.poster" src="../../assets/img/noimg.png" class="card-img img-img" style="width:100%"></div>
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
              </b-tab>

              <b-tab title="찜한 영화">
                <div class="row">
                  <div class="card text-white col-12 col-sm-6 col-md-4 col-lg-3 p-4 imgHoverEvent event2" style="border:none; background-color:black" v-for="movie in likedMovieData" :key="movie.id">
                    <div class="imgBox"><img v-if="movie.poster" :src="movie.poster" class="card-img img-img" style="width:100%"></div>
                    <div class="imgBox"><img v-if="!movie.poster" src="../../assets/img/noimg.png" class="card-img img-img" style="width:100%"></div>
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
              </b-tab>
            </b-tabs>
          </div>

          
          <!-- <div class="card text-white col-12 col-sm-6 col-md-4 col-lg-3 p-3 imgHoverEvent event2" style="border:none; background-color:black" v-for="movie in movieData" :key="movie.id">
            <div class="imgBox"><img v-if="movie.poster" :src="movie.poster" class="card-img img-img" style="width:100%"></div>
            <div class="imgBox"><img v-if="!movie.poster" src="../../assets/img/noimg.png" class="card-img img-img" style="width:100%"></div>
            <div class="card-img-overlay hoverBox">
              <span class="movie-text">
                <p class="card-title p1" style="font-size:1.5rem; color:crimson; font-weight:bold; margin-top:50%">{{movie.title}}</p>
                <div class="d-flex justify-content-center">
                  <button @click="goDetail(movie.movie_id)" class="btn btn-defualt" style="border:1px red solid; border-radius:10px"><span style="font-weight:bold; color:white;">view</span></button>
                </div>
              </span>
            </div>
          </div> -->
        </div>
      </div>
    </div>
  <Update />
  </div>
</template>

<script>
import Update from '../../components/update/UpdateModal'
import axios from "axios";
import constants from "../../lib/constants";

export default {
  name: "Profile",
  components:{
    Update
  },
  data: () => {
    return {
      profileData: {},
      ratedMovieData:{}, // 평가 한 영화
      likedMovieData:{},  // 찜한 영화
      ratedMovieCnt:0,
      likedMovieCnt:0,
    };
  },
  created() {
    this.adminCheck();
  },
  methods: {
    adminCheck() {
      if (this.$cookies.isKey("auth-token")){
        const config = {
          headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
        }
        axios
        .get(`${constants.SERVER_URL}/accounts/userdetail/`,config)
        .then((res) => {
          this.ratedMovieData=res.data.rated_movie_data
          this.likedMovieData=res.data.liked_movie_data
          this.profileData=res.data.user_data
          this.ratedMovieCnt=res.data.rated_movie_cnt
          this.likedMovieCnt=res.data.liked_movie_cnt
        })
        .catch((err) => {
          console.log(err);
        });
      }
    },
    goDetail(id) {
        this.$router.push(`/movie/${id}`).catch(() => {
            this.$router.go()
        })
    },

  logout() {
    const axiosConfig ={
      headers:{
        Authorization : `Token ${this.$cookies.get('auth-token')}`
      },
    }
    axios.post(constants.SERVER_URL + '/rest-auth/logout/',null,axiosConfig)
    .then(()=>{
      this.$cookies.remove('auth-token')
      this.isLoggedIn=false
      this.$router.go()
      this.$router.push({name:constants.URL_TYPE.MAIN})
    })
    .catch((error)=>{
      console.log(error.response.data)
    })
  },
  },
};
</script>

<style scoped>

.img-img{height: 20rem; width: 100%; }
        .imgHoverEvent{position: relative; overflow: hidden; display: inline-block;}
        .imgHoverEvent .imgBox{text-align: center; background-size: auto 100%;}
        .imgHoverEvent .hoverBox{position: absolute; width: 100%; height: 100%;}
        .hoverBox p.p1{text-align:center; font-size:18px;}
        .hoverBox p.p2{text-align:center; margin-top: 40px;}
        .event1 .hoverBox{background: linear-gradient(to bottom, rgba(0,0,0,0) 5%,rgb(15, 15, 15) 90%); transform: translateY(75%); transition: 0.5s;}
        .event1:hover .hoverBox{transform: translateY(0);}

        .event2 .imgBox{filter: blur(0)}
        .event2:hover .imgBox{filter: blur(5px) grayscale(60%); transition: 0.5s;}
        .event2 .hoverBox .movie-text {visibility: hidden; }
        .event2:hover .hoverBox .movie-text {visibility: visible;}
</style>