import Vue from 'vue'
import VueRouter from 'vue-router'
import constants from '../lib/constants.js'

// main
import Main from '../views/main/Main.vue'

// User
import Join from '../views/user/Join.vue'
import Profile from '../views/user/Profile.vue'

// Movie
import Movie from '../views/movie/Movie.vue'
import MovieDetail from '../views/movie/MovieDetail.vue'
import MovieRecommend from '../views/movie/MovieRecommend.vue'

// review
import ReviewCreate from '../views/review/ReviewCreate'
import ReviewUpdate from '../views/review/ReviewUpdate'
import ReviewDetail from '../views/review/ReviewDetail'

// search
import SearchMovie from '../views/search/SearchMovie.vue'

Vue.use(VueRouter)

const routes = [
    // main
    {
        path: '/',
        name: constants.URL_TYPE.MAIN,
        component: Main,
    },
    // User
    {
        path: '/user/join',
        name: "Join",
        component: Join,
    },
    {
        path: "/user/profile",
        name: constants.URL_TYPE.USER.PROFILE,
        component: Profile,
    },

    // movie
    {
        path: "/movie",
        name: "Movie",
        component: Movie
    },
    {
        path: "/movie/:movie_pk",
        name: constants.URL_TYPE.MOVIE.DETAIL,
        component: MovieDetail,
    },
    {
        path: "/movierecommend",
        name: "MovieRecommend",
        component: MovieRecommend,
    },

    //review
    {
        path: "/:movie_pk/review/create",
        name: "ReviewCreate",
        component: ReviewCreate,
    },
    {
        path: "/:review_pk/review/update",
        name: "ReviewUpdate",
        component: ReviewUpdate,
    },
    {
        path: "/:review_pk/review/detail",
        name: "ReviewDetail",
        component: ReviewDetail,
    },
    // search
    {
        path: "/searchmovie",
        name: "SearchMovie",
        component: SearchMovie,
    },

]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router