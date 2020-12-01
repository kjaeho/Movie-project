<template>
  <div class="container col-md-10 mt-5">
    <svg class="my-auto" id="Capa_1" enable-background="new 0 0 511.975 511.975" height="100" viewBox="0 0 511.975 511.975" width="100" xmlns="http://www.w3.org/2000/svg"><g><path d="m145.892 289.718h96.167v56.569h-96.167z" fill="#c8885e" transform="matrix(.707 -.707 .707 .707 -168.048 230.302)"/><path d="m155.892 313.86h96.167v28.284h-96.167z" fill="#9f5f4e" transform="matrix(.707 -.707 .707 .707 -172.19 240.302)"/><path d="m202.585 394.613-99.75 99.739c-11.75 11.75-27.18 17.62-42.61 17.62s-30.85-5.87-42.6-17.62c-23.5-23.489-23.5-61.72 0-85.21l99.74-99.75c5.86-5.85 15.36-5.85 21.22 0l64 64c5.85 5.861 5.85 15.361 0 21.221z" fill="#fed843"/><path d="m202.585 373.392c5.85 5.86 5.85 15.36 0 21.221l-99.75 99.739c-11.75 11.75-27.18 17.62-42.61 17.62s-30.85-5.87-42.6-17.62l152.96-152.96z" fill="#fabe2c"/><path d="m511.975 183.003c0 100.91-82.09 183-183 183-50.46 0-96.2-20.52-129.34-53.66s-53.66-78.88-53.66-129.34c0-100.91 82.09-183 183-183 50.46 0 96.2 20.52 129.34 53.66 33.14 33.139 53.66 78.88 53.66 129.34z" fill="#d5e8fe"/><path d="m511.975 183.003c0 100.91-82.09 183-183 183-50.46 0-96.2-20.52-129.34-53.66l258.68-258.68c33.14 33.139 53.66 78.88 53.66 129.34z" fill="#b5dbff"/><path d="m458.315 53.663c-33.14-33.141-78.88-53.66-129.34-53.66-100.91 0-183 82.09-183 183 0 50.46 20.52 96.2 53.66 129.34 33.14 33.141 78.88 53.66 129.34 53.66 100.91 0 183-82.09 183-183 0-50.46-20.52-96.201-53.66-129.34zm-129.34 282.34c-42.18 0-80.43-17.16-108.14-44.86-27.7-27.71-44.86-65.96-44.86-108.14 0-84.36 68.64-153 153-153 42.18 0 80.43 17.16 108.14 44.86 27.7 27.71 44.86 65.96 44.86 108.14 0 84.36-68.64 153-153 153z" fill="#979fef"/><path d="m511.975 183.003c0 100.91-82.09 183-183 183-50.46 0-96.2-20.52-129.34-53.66l21.2-21.2c27.71 27.7 65.96 44.86 108.14 44.86 84.36 0 153-68.64 153-153 0-42.18-17.16-80.43-44.86-108.14l21.2-21.2c33.14 33.139 53.66 78.88 53.66 129.34z" fill="#7984eb"/><g><path d="m396.145 126.173c-1.75-1.75-3.61-3.34-5.58-4.76-17.73-12.9-43.49-12.641-61.59 5.47-20.17-20.17-49.64-18.25-67.17-.71-18.33 18.32-18.42 48.05-.01 66.47l28.77 28.771 27.8 27.79c5.86 5.859 15.36 5.859 21.21.01.09-.09.17-.17.23-.229.07-.07.25-.25.25-.25 1.77-1.771 11.52-11.521 56.09-56.091 18.38-18.372 18.37-48.101 0-66.471z" fill="#ff73a5"/></g><path d="m396.145 192.642c-44.57 44.57-54.32 54.32-56.09 56.091 0 0-.18.18-.25.25-.06.06-.14.14-.23.229-5.85 5.85-15.35 5.85-21.21-.01l-27.8-27.79 100-100c1.97 1.42 3.83 3.01 5.58 4.76 18.37 18.371 18.38 48.1 0 66.47z" fill="#ff468c"/></g></svg>
    <span class="my-auto ml-3" style="color:red; font-size:3rem; font-weight:bold;">{{this.$cookies.get('searchKeyword')}}</span>
    <span class="ml-2" style="color:white; font-size:1.5rem; font-weight:bold; ">과(와) 관련된 영화 검색 결과 :)</span>
    <div v-if="searchMovie.length > 0">
        <div v-for="movie in searchMovie" :key="movie.id" class="card m-4 text-white imgHoverEvent event2" style="width:12rem; display:inline-block; border:none; border-radius:10px;">
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
    <div v-else>
        <div class="d-flex justify-content-center" style="margin-top:15%">
            <svg id="Capa_1" enable-background="new 0 0 512 512" height="200" viewBox="0 0 512 512" width="200" xmlns="http://www.w3.org/2000/svg"><g><path d="m512 256c0 141.385-114.615 256-256 256s-256-114.615-256-256 114.615-256 256-256 256 114.615 256 256z" fill="#f44545"/><path d="m448.66 256c0 106.403-86.257 192.66-192.66 192.66s-192.66-86.257-192.66-192.66 86.257-192.66 192.66-192.66 192.66 86.257 192.66 192.66z" fill="#fb5858"/><path d="m206 349.364c0 10.217-33.131 18.5-74 18.5s-74-8.283-74-18.5 33.131-18.5 74-18.5 74 8.283 74 18.5zm150.702 116.381c0 10.217-33.131 18.5-74 18.5s-74-8.283-74-18.5 33.131-18.5 74-18.5 74 8.283 74 18.5z" fill="#c42d2d"/><path d="m291 69v186c0 22.091-17.909 40-40 40h-92.037l-19.853 43.868c-3.546 7.836-14.675 7.836-18.221 0l-19.852-43.868h-40.037c-22.091 0-40-17.909-40-40v-186c0-22.091 17.909-40 40-40h190c22.091 0 40 17.909 40 40z" fill="#ffc14f"/><path d="m301 69v186c0 22.091-17.909 40-40 40h-17c-73.454 0-133-59.546-133-133 0-73.454 59.546-133 133-133h17c22.091 0 40 17.909 40 40z" fill="#fff36c"/><path d="m217.816 213.429c3.905 3.905 3.905 10.237 0 14.143-1.953 1.953-4.512 2.929-7.071 2.929s-5.118-.976-7.071-2.929l-57.929-57.929-57.929 57.929c-1.953 1.953-4.512 2.929-7.071 2.929s-5.118-.976-7.071-2.929c-3.905-3.905-3.905-10.237 0-14.143l57.929-57.929-57.929-57.929c-3.905-3.905-3.905-10.237 0-14.143 3.906-3.905 10.236-3.905 14.143 0l57.929 57.929 57.929-57.929c3.906-3.905 10.236-3.905 14.143 0 3.905 3.905 3.905 10.237 0 14.143l-57.93 57.929z" fill="#464646"/><path d="m449.511 190v186c0 22.091-17.909 40-40 40h-90.548l-19.853 43.868c-3.546 7.836-14.675 7.836-18.221 0l-19.852-43.868h-20.037c-22.091 0-40-17.909-40-40v-186c0-22.091 17.909-40 40-40h168.511c22.091 0 40 17.909 40 40z" fill="#c8e2fd"/><path d="m491 190v186c0 22.091-17.909 40-40 40h-47c-73.454 0-133-59.546-133-133 0-73.454 59.546-133 133-133h47c22.091 0 40 17.909 40 40z" fill="#e9f3fe"/><path d="m321.906 233.49.91 94.112c0 5.458-3.01 9.91-7.667 11.365-4.542 1.419-9.357-.384-12.27-4.591l-48.31-69.956v66.556c0 5.27-4.287 9.556-9.556 9.556s-9.556-4.287-9.556-9.556v-97.211c0-4.205 2.697-7.871 6.712-9.123 4.019-1.249 8.322.235 10.709 3.693l50.573 73.235-.657-67.894c-.024-2.553.946-4.962 2.733-6.785 1.788-1.822 4.178-2.839 6.73-2.864h.094c5.219 0 9.505 4.245 9.555 9.463zm134.637 50.23c0 32.121-26.132 58.253-58.253 58.253-32.12 0-58.252-26.132-58.252-58.253s26.132-58.253 58.252-58.253c32.121 0 58.253 26.132 58.253 58.253zm-19.112 0c0-21.582-17.559-39.14-39.141-39.14s-39.14 17.558-39.14 39.14 17.558 39.141 39.14 39.141 39.141-17.559 39.141-39.141z" fill="#3f7196"/></g></svg>
            <div @click="goMain" style="cursor:pointer;">
                <span class="my-auto ml-4" style="font-weight:bold; font-size: 4rem; color:white;">검색 결과가 없습니다 (-_-)</span>
                <br>
                <span class="ml-4" style="font-weight:bold; font-size: 4rem; color:red; display:inline-block">MAIN</span>
                <span class="" style="font-weight:bold; font-size: 4rem; color:white;">으로 돌아가기</span>
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
            searchMovie: [],
        }
    },
    methods: {
        callSearch() {
            let searchKeyword = this.$cookies.get('searchKeyword')
            axios.get(`${constants.SERVER_URL}/movies/movie-serach/${searchKeyword}/`)
                .then((res) => {
                    console.log(res.data)
                    this.searchMovie = res.data
                })
        },
        goDetail(id) {
            this.$router.push(`/movie/${id}`).catch(() => {
                this.$router.go()          
            })
        },
        goMain() {
            this.$router.push('/').catch(() => {
                this.$router.go()
            })
        },
    },
    created(){
        this.callSearch()
    },
}
</script>

<style>

</style>