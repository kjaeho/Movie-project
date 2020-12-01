<template>
  <div>
    <div>{{ reviewData }}</div>
  </div>
</template>

<script>
// import CommentList from '@/views/review/CommentList'
import axios from 'axios'
import constants from '../../lib/constants'

export default {
  components: {
  },
  data(){
    return{
      reviewData:'',
    }
  },
  methods:{
    getReviewData(){
      axios.get(constants.SERVER_URL+`/reviews/${this.$route.params.review_pk}/review-detail/`)
        .then((res)=>{
          this.reviewData=res.data
        })
        .catch((err)=>{
          console.log(err)
        })
    },
  },
  created(){
    this.getReviewData()
  }
}
</script>

<style>

</style>