<template>
    <div class="container col-md-10">

        <!-- 검색기능 -->

        <div class="dropdown mt-5">
          <button class="dropbtn" @click="resetMovieData"><span style="font-weight:bold">ALL</span></button>
          <!-- <div class="dropdown-content">
            <a>Link 1</a>
            <a>Link 2</a>
            <a>Link 3</a>
          </div> -->
        </div>
        <div class="dropdown">
          <button v-if="!choiceNation" class="dropbtn"><span style="font-weight:bold">국가</span></button>
          <button v-if="choiceNation" class="dropbtn"><span style="font-weight:bold">{{choiceNation}} 영화</span></button>
          <div class="dropdown-content">
            <a @click="selectNation('한국')">한국 영화</a>
            <a @click="selectNation('해외')">외국 영화</a>
          </div>
        </div>
        <div class="dropdown">
          <button v-if="!choiceGenre" class="dropbtn"><span style="font-weight:bold">장르</span></button>
          <button v-if="choiceGenre" class="dropbtn"><span style="font-weight:bold">{{choiceGenre}}</span></button>
          <div class="dropdown-content-genre">
            <a @click="selectGenre('SF')">SF</a>
            <a @click="selectGenre('가족')">가족</a>
            <a @click="selectGenre('공연실황')">공연실황</a>
            <a @click="selectGenre('공포')">공포</a>
            <a @click="selectGenre('느와르')">느와르</a>
            <a @click="selectGenre('다큐멘터리')">다큐멘터리</a>
            <a @click="selectGenre('드라마')">드라마</a>
            <a @click="selectGenre('로맨스')">멜로/로맨스</a>
            <a @click="selectGenre('모험')">모험</a>
            <a @click="selectGenre('무협')">무협</a>
            <a @click="selectGenre('뮤지컬')">뮤지컬</a>
            <a @click="selectGenre('미스터리')">미스터리</a>
            <a @click="selectGenre('범죄')">범죄</a>
            <a @click="selectGenre('블랙코미디')">블랙코미디</a>
            <a @click="selectGenre('서부')">서부</a>
            <a @click="selectGenre('서사')">서사</a>
            <a @click="selectGenre('서스펜스')">서스펜스</a>
            <a @click="selectGenre('스릴러')">스릴러</a>
            <a @click="selectGenre('실험')">실험</a>
            <a @click="selectGenre('애니메이션')">애니메이션</a>
            <a @click="selectGenre('액션')">액션</a>
            <a @click="selectGenre('전쟁')">전쟁</a>
            <a @click="selectGenre('컬트')">컬트</a>
            <a @click="selectGenre('코미디')">코미디</a>
            <a @click="selectGenre('판타지')">판타지</a>
          </div>
        </div>
        <div class="dropdown">
          <button v-if="!choiceYear" class="dropbtn"><span style="font-weight:bold">연도</span></button>
          <button v-if="choiceYear" class="dropbtn"><span style="font-weight:bold">{{choiceYear}}0년대 영화</span></button>
          <div class="dropdown-content">
            <a @click="selectYear('195')">1950년대 영화</a>
            <a @click="selectYear('196')">1960년대 영화</a>
            <a @click="selectYear('197')">1970년대 영화</a>
            <a @click="selectYear('198')">1980년대 영화</a>
            <a @click="selectYear('199')">1990년대 영화</a>
            <a @click="selectYear('200')">2000년대 영화</a>
            <a @click="selectYear('201')">2010년대 영화</a>
            <a @click="selectYear('202')">2020년대 영화</a>
          </div>
        </div>
        <div class="dropdown">
          <button v-if="rorb" class="dropbtn"><span style="font-weight:bold">최신순</span></button>
          <button v-if="!rorb" class="dropbtn"><span style="font-weight:bold">평점순</span></button>
          <div class="dropdown-content">
            <a @click="getSpecificData(1)">최신순</a>
            <a @click="getSpecificData(0)">인기순</a>
          </div>
        </div>
        <!-- 선택한 장르 나타내기 -->
        <div v-if="choiceNation || choiceGenre || choiceYear" class="p-3">
          <i class="fas fa-search-plus" style="color:white; font-size:1.4rem"><span class="ml-2">Category 검색 결과 :</span></i>
          <span v-if="choiceYear" style="color:white; font-size:1.4rem; font-weight:bold" class="ml-2">{{choiceYear}}0 년대</span>
          <span v-if="choiceNation" style="color:white; font-size:1.4rem; font-weight:bold" class="ml-2">{{choiceNation}}</span>
          <span v-if="choiceGenre" style="color:white; font-size:1.4rem; font-weight:bold" class="ml-2">{{choiceGenre}} 영화</span>
        </div>

        <!-- 영화 리스트 보여주기 -->
        <div v-if="movieData">
          <div class="card text-white col-12 col-sm-6 col-md-4 col-lg-3 p-4 imgHoverEvent event2" style="border:none; background-color:black" v-for="movie in movieData" :key="movie.id">
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

        <div v-if="movieData.length == 0" class="d-flex justify-content-center" style="margin:10rem">
          <span style="color:white; font-weight:bold; font-size:2rem">검색 결과가 없습니다 :)</span>
        </div>


        <!-- pagination -->
        <div v-if="flag" class="mt-3">
          <b-pagination v-model="currentPage" :total-rows="rows" align="center" style="text-color:red"></b-pagination>
        </div>

        <div v-if="!flag" class="mt-3">
          <b-pagination v-model="currentPageForSpecific" :total-rows="rows" align="center" style="text-color:red"></b-pagination>
        </div>



    </div>
</template>

<script>
import axios from 'axios'
import constants from '../../lib/constants'


export default {
    data() {
        return {
            movieData:{},
            genre: 0,
            movieNation:0,
            movieGenre:0,
            movieYear:0,
            rows:'',
            currentPage:1,
            currentPageForSpecific:1,
            flag:true,
            choiceNation: "",
            choiceGenre: "",
            choiceYear: "",
            rorb:1
        }
    },
    created(){
      this.getData(this.rorb)  
    },
    methods:{
        getData(f) {
          if(f){
            this.rorb=1
          }else{
            this.rorb=0
          }
          this.flag=true
          this.currentPageForSpecific=1
          console.log(this.rorb)
          axios.get(constants.SERVER_URL + `/movies/recent-list/${this.currentPage}/${this.rorb}/`)
            .then((res) => {
                this.movieData = res.data.movieData
                this.rows=res.data.pageNum*20
            })
            .catch((err)=>{
                console.log(err)
            })
        },
        getSpecificData(num){
          const genre=this.movieGenre
          const nation=this.movieNation
          const year=this.movieYear
          this.flag=false
          this.currentPage=1
          this.rorb=num
          console.log(num)
          axios.get(constants.SERVER_URL+`/movies/listby-category/${genre}/${nation}/${year}/${this.currentPageForSpecific}/${num}/`)
            .then((res)=>{
              this.movieData=res.data.movieData
              this.rows=res.data.pageNum*20
            })
            .catch((err)=>{
              console.log(err)
            })

        },
        resetMovieData(){
          this.movieGenre=0
          this.movieNation=0
          this.movieYear=0
          this.choiceNation = ""
          this.choiceGenre = ""
          this.choiceYear = ""
          this.getData(this.rorb)
        },
        goDetail(id) {
            this.$router.push(`/movie/${id}`).catch(() => {
                this.$router.go()          
            })
        },
        selectNation(nation) {
          this.movieNation = nation
          this.choiceNation = nation
          this.getSpecificData(this.rorb)
        },
        selectGenre(genre) {
          this.movieGenre = genre
          this.choiceGenre = genre
          this.getSpecificData(this.rorb)
        },
        selectYear(year) {
          this.movieYear = year
          this.choiceYear = year
          this.getSpecificData(this.rorb)
        },
        resetsPage(){
          if (this.currentPageForSpecific>=2){
            this.currentPageForSpecific=1
          }
        },
        
    },
    watch:{
      currentPage(){
        this.getData(this.rorb)
      },
      currentPageForSpecific(){
        this.getSpecificData(this.rorb)
      },
      movieGenre(){
        this.resetsPage()
      },
      movieNation(){
        this.resetsPage()
      },
      movieYear(){
        this.resetsPage()
      },
    }
}
</script>

<style>
/* .img-img{min-height: 100%; max-width: 100%; } */
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
        /* .event2 .hoverBox span{display: block; position: absolute; width:100%; top: 50%; transform: translateY(-50%)}
        .event2 .hoverBox span p.p2{text-align: center;} */

/* Style The Dropdown Button */
.dropbtn {
  width: 100%;
  background-color: black;
  color: whitesmoke;
  padding: 16px;
  font-size: 16px;
  border: none;
  cursor: pointer;
  border:none
}

/* The container <div> - needed to position the dropdown content */
.dropdown {
  width:25%;
  position: relative;
  display: inline-block;
  
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: gray;
  min-width: 100%;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

/* Links inside the dropdown */
.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

/* Change color of dropdown links on hover */
.dropdown-content a:hover {background-color: whitesmoke; cursor: pointer;}

/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {
  background-color: black;
  display: block;
  color:red
}

/* Change the background color of the dropdown button when the dropdown content is shown */
.dropdown:hover .dropbtn {
  background-color: whitesmoke;
  color: red;
}
.dropdown-content-genre {
  display: none;
  position: absolute;
  background-color: gray;
  min-width: 100%;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}
.dropdown-content-genre a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: inline-block;
}
.dropdown:hover .dropdown-content-genre {
  background-color: black;
  display: block;
  color:red
}
.dropdown-content-genre a:hover {background-color: whitesmoke; cursor: pointer;}
</style>