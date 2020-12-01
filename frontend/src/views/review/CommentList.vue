<template>
  <div>
    <input type="text" v-model="commentData.content">
    <button @click="createComment">작성하기</button>
    {{ commentList}}
    <div v-for="comment in commentList" :key="comment.id">
      <div>{{comment}}
      <!-- <div v-if="userData.email==review.writer.email"> -->
        <button v-if="!flag" @click="flag=true">댓글 수정</button>
        <input type="text" v-if="flag" v-model="commentData.content">
        <button v-if="flag" @click="updateComment(comment.id)">수정완료</button>
        <button @click="deleteComment(comment.id)">댓글 삭제</button>
      <!-- </div> -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import constants from '../../lib/constants'

export default {
  data(){
    return{
      commentData:{
        content:'',
      },
      commentList:'',
      flag:true,
    }
  },
  methods:{
    getCommentList(){
      axios.get(constants.SERVER_URL+`/reviews/${this.$route.params.review_pk}/comment-list/`)
        .then((res)=>{
          this.commentList=res.data
        })
        .catch((err)=>{
          console.log(err)
        })
    },
    createComment(){
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(constants.SERVER_URL+`/reviews/${this.$route.params.review_pk}/create-comment/`,this.commentData,config)
        .then(()=>{})
        .catch((err)=>{
          console.log(err.response.data)
        })
    },
    updateComment(id){
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(constants.SERVER_URL+`/reviews/${id}/update-comment/`,this.commentData,config)
        .then(()=>{
          this.flag=false
        })
        .catch((err)=>{
          console.log(err.response.data)
        })
    },
    deleteComment(id){
      axios.delete(constants.SERVER_URL+`/reviews/${id}/delete-comment/`)
        .then(()=>{
          this.getCommentList()
        })
        .catch((err)=>{
          console.log(err)
        })
    },
  },
  created(){
    this.getCommentList()
  },
}
</script>

<style>

</style>