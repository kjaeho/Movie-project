<template>
  <div class="container m-5 mx-auto w-75">
    <!-- 영화 상세정보 -->
    <div class="card shadow p-3">
      <div class="card-body">
        <div class="row">
          <div class="col-8 col-md-6 col-sm-4">
            <h3 class="text-left font-weight-bold" style="font-family: 'Black Han Sans', sans-serif;">{{ movieData.title }}</h3>
            <small class="float-left">{{ movieData.titleorigin }}, </small>
            <!-- <small class="d-flex inline">{{movieData.releasedate}}</small> -->
          </div>
          <div v-if="!hasRated" class="ml-auto my-auto">
            <b-icon style="cursor:pointer" v-if="!isLiked" @click="rateMovie(false)" font-scale="2" class="my-auto ml-auto mr-4" variant="danger" icon="heart"></b-icon>
            <b-icon style="cursor:pointer" v-else @click="cancelRating(1)" font-scale="2" class="my-auto ml-auto mr-4" variant="danger" icon="heart-fill"></b-icon>
          </div>

        </div>
        <hr />
        <div class="card-body row">
          <div class="d-flex flex-column col-8 p-0">
            <div class="float-left">
              <p class="float-left font-weight-bold pr-3">장르</p>
              <div
                class="float-left"
                v-for="genre in movieData.genres"
                :key="genre.id"
              >
                <b-badge class="mr-1">{{ genre }}</b-badge>
              </div>
            </div>
            <div class="float-left">
              <p class="float-left font-weight-bold pr-3">개봉일</p>
              <p class="float-left">{{ movieData.releasedate }}</p>
            </div>
            <!-- <div class="float-left"> -->
              <!-- <p class="float-left font-weight-bold pr-3">등급</p> -->
              <!-- <p v-if="movie.adult" class="float-left"> 청소년 관람불가</p> -->
              <!-- <p v-if="!movie.adult" class="float-left"> 청소년 관람가능</p> -->
            <!-- </div> -->
            <div class="d-flex float-left align-items-center">
              <p class="float-left font-weight-bold pr-3">평점</p>
              <p v-if="!movieData.ravg" class="font-weight-bold text-secondary text-left">이 영화의 평가가 아직 없습니다.</p>
              <p v-else class="float-left text-left pr-3"><small class="align-items-center"><star-rating :show-rating="true" :star-size="22" :rating="movieData.ravg" :read-only="true" :increment="0.5" class="h6"></star-rating></small> <p v-if="movieData.rcnt"> | {{ movieData.rcnt }}명</p>
              <b-button v-if="hasRated" class="ml-3 mt-1 mb-auto font-weight-bold" size="sm" variant="danger" @click="cancelRating(2)">취소</b-button>
            </div>
            <div class="float-left">
              <p class="float-left font-weight-bold pr-3">감독</p>
              <p class="float-left">{{ movieData.director }}</p>
            </div>
            <div class="float-left">
              <p class="float-left font-weight-bold pr-3">배우</p>
              <div
                class="float-left"
                v-for="actor in movieData.actors"
                :key="actor.id"
              >
                <b-badge variant="light" class="mr-2">{{ actor }}</b-badge>
              </div>
            </div>
            <div class="float-left">
              <p class="float-left font-weight-bold pr-3">줄거리</p>
              <p class="float-left text-left pr-3">{{ movieData.plot }}</p>
            </div>
            <br />
            <div class="float-left">
              <!-- <p class="float-left font-weight-bold pr-3"></p> -->
              <div
                class="float-left"
                v-for="keyword in movieData.keywords"
                :key="keyword.id"
              >
                <b-badge variant="light" class="mr-2">#{{ keyword }}</b-badge>
              </div>
            </div>
          </div>
          <img
            :src="movieData.poster"
            alt="movie poster"
            class="card-img h-100 float-right col-4 p-0"
          />
          <!-- <div>
            <div>
            
                <button class="btn btn-default" title="click">
                  <b-icon v-b-modal.modal-multi-1 icon="camera-video" font-scale="2" animation="throb" ></b-icon>
                  </button>
              
              <b-modal
                id="modal-multi-1"
                class="modal-dialog"
                title="First Modal"
                ok-only
                no-stacking
                hide-footer
                hide-header
                centered
                modalbackdrop
                bg-transparent
                body-bg-transparent
                style="background:none; cursor:pointer;"
              >
                <iframe :src="movieData.video" class="d-flex align-content-center" style="width:50vw; height:27vw;"></iframe>
              </b-modal>
            </div>
          </div> -->
        </div>
      </div>
    </div>

    <div v-if="!hasRated" class="card p-3 mt-3">
      <div>
        <div>
          <h3 class="mt-2 pl-3 text-left font-weight-bold" style="font-family: 'Black Han Sans', sans-serif;">이 영화의 평점을 남겨주세요!</h3>
        </div>
        <div class="text-center my-4">
          <div @mouseleave="showCurrentRating(0)" style="display:inline-block;">
              <star-rating :star-size="50" v-model="currentSelectedRating" :show-rating="false" @current-rating="showCurrentRating" @rating-selected="setCurrentSelectedRating" :increment="0.5"></star-rating>
          </div>
        </div>
      </div>
    </div>

    <!-- 리뷰  -->
    <div class="card shadow p-3 mt-3">
      <div class="row">
        <div class="col-7">
          <h3 class="pl-3 mt-2 text-left font-weight-bold" style="font-family: 'Black Han Sans', sans-serif;">Reviews</h3>
        </div>
        <div class="ml-auto my-auto col-4 text-right mt-2 mr-2">
          <!-- <button class="p-0 bg-transparent border-0" data-toggle="modal" data-target="#ReviewCreate"> -->
            <b-icon
              style="cursor:pointer;"
              icon="pen"
              variant="secondary"
              aria-hidden="true"
              font-scale="1.5"
              data-toggle="modal" data-target="#ReviewCreate"
            ></b-icon>
          <!-- </button> -->
        </div>
      </div>
      <hr />

      <div class="px-3 pt-0 d-flex inline">
        <ReviewList/>
      </div>
    </div>
    </div>
  <!-- </div> -->
</template>

<script>
import constants from "../../lib/constants";
import axios from "axios";
import ReviewList from "@/views/review/ReviewList"
import Swal from 'sweetalert2'

// import CommentList from "@/views/review/CommentList"
import StarRating from 'vue-star-rating'


export default {
  name: "MovieDetail",
  components:{
    ReviewList,
    StarRating
  },
  data: () => {
    return {
      moive_pk:'',
      movieData: {},
      reviewData: {},

      isLiked:false,
      hasRated:false,
      activateRate:true,
      
      rating: 0,
      currentRating: 0,
      currentSelectedRating: 0,

    };
  },
  created() {
    this.getDetail()
    this.getUserRating()
  },
  methods: {
    setRating: function(rating) {
        this.rating = rating
    },
    showCurrentRating: function(rating) {
        this.currentRating = (rating === 0) ? this.currentSelectedRating : rating*2
    },
    setCurrentSelectedRating: function(rating) {
      this.currentSelectedRating = rating
      this.rateMovie(true)
    },
    getDetail() {
      this.movie_pk = this.$route.params.movie_pk;
      axios
        .get(`${constants.SERVER_URL}/movies/${this.movie_pk}/`)
        .then((res) => {
          this.movieData = res.data[0];
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getUserRating(){
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get(constants.SERVER_URL+`/movies/get-rating/${this.$route.params.movie_pk}/`,config)
        .then((res)=>{
          console.log(res.data.star)
          if(res.data.star){
            this.currentSelectedRating=res.data.star
            if(res.data.star===-1){
              this.isLiked=true
              this.hasRated=false
            }else{
              this.hasRated=true
            }
          }else{
            this.hasRated=false
            this.isLiked=false
            this.currentSelectedRating=0
          }
        })
        .catch((err)=>{
          console.log(err)
        })
    },
    rateMovie(flag){
      if (this.$cookies.get('auth-token')) {
        const config = {
          headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
        }
        var ratingData={
          star:''
        }
        if(flag){
          ratingData.star=this.currentSelectedRating
        }else{
          ratingData.star=-1
        }
        axios.post(constants.SERVER_URL+`/movies/rate-movie/${this.$route.params.movie_pk}/`,ratingData,config)
          .then(()=>{
            this.getUserRating()
            this.getDetail()
          })
          .catch((err)=>{
            console.log(err)
          })
      } else {
        Swal.fire({
          icon: 'error',
          text: '로그인 후 이용해주세요...',
          confirmButtonColor: '#fff',
          width: 350,
          confirmButtonText: '<a data-toggle="modal" data-target="#Login" style="font-size:1rem; color:black; font-weight:bold;">로그인</a>',
          showCancelButton: true,
          cancelButtonText: '<a style="font-size:1rem; font-weight:bold; color:black">취소</a>',
          cancelButtonColor: '#fff',
        }).then(() => {
          Swal.close();
        });
      }
    },
    cancelRating(tmp){
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      const data = {
        flag:tmp
      }
      axios.post(constants.SERVER_URL+`/movies/cancel-rating/${this.$route.params.movie_pk}/`,data,config)
        .then(()=>{
          this.getUserRating()
          this.getDetail()
        })
        .catch((err)=>{
          console.log(err)
        })
    },
  },
};
</script>

<style>
/* .modal-dialog { 
  background-color: transparent;
  min-width: 100%; height: 100vh; margin: 0; padding: 0; } */

.modal-content {
  background-color: black;
}


#modal-multi-1 {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
}

</style>