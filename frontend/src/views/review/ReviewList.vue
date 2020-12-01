<template>
  <div class="w-100">
    <!-- <button @click="goCreateReview">리뷰 작성하기</button> -->
    <!-- <p>{{ this.reviewList }}</p> -->


    <div v-for="review in reviewList" :key="review.id" class="card p-3 mt-2">
      <div>
        <div class="d-flex">
          <p class="font-weight-bold mb-0 mr-2">{{ review.summary }}</p>
          <b-badge v-if="review.spo" class="my-auto" variant="danger">스포</b-badge>
          <small v-if="review.writer.email!=user" class="ml-auto">{{ review.writer.username }}</small>
          <div v-else class="ml-auto">
            <ReviewUpdate :reviewId="review.id" @reRender="getReviewList"/>
            <i style="cursor:pointer" class="mr-2 fas fa-edit" data-toggle="modal" data-target="#ReviewUpdate"></i>
            <i style="cursor:pointer" @click="deleteReview(review.id)" class="fas fa-trash-alt"></i>
          </div>
        </div>

        <!-- # 리뷰랑 댓글보기 -->
        <small v-if="!flag1" style="cursor:pointer; font-weight:bold;" class="my-1" @click="getReviewDetail1(review.id)">더보기 <i class="fas fa-arrow-down"></i></small>
      </div>

      <div v-if="flag1 && review.id == reviewid">
        <hr>
        <div>
          <div class="d-flex justify-content-between">
            <p style="text-align:justify; width:50%">{{ review.content }}</p>
            <i @click="foldReview" class="fas fa-level-up-alt" style="cursor:pointer"><small class="ml-1" style="font-weight:bold;">접기</small></i>
          </div>

        <div class="d-flex justify-content-between">
          <!-- <input type="text" style="width:80%; display:inline-block" class="form-control" v-model="commentData.content"/> -->
          <!-- <button class="btn btn-defualt my-auto" style="border:1px solid black; border-radius:10px;" @click="createComment(review.id)"><span style="font-weight:bold;">댓글 작성</span></button> -->
        </div>

        <div v-for="comment in commentList" :key="comment.id">
          <div>
            {{comment.content}}
            <br>
            <button v-if="flag" @click="isCommentUpdate(comment.id, comment.content)">댓글 수정</button>
            <textarea v-if="isComment && comment.id == commentid" v-model="updatecommentData.content"></textarea>
            <p @click="updateComment(comment.id,review.id)">수정완료</p>
            <button v-if="flag" @click="deleteComment(comment.id)">댓글 삭제</button>
            <hr>
          </div>
        </div>
      </div>
      </div>
    </div>
    <ReviewCreate @reRender="getReviewList"/>
  </div>
</template>

<script>
import axios from "axios";
import constants from "../../lib/constants";
import ReviewUpdate from "@/views/review/ReviewUpdate"
import ReviewCreate from "@/views/review/ReviewCreate"
import Swal from 'sweetalert2'
// import ReviewDetail from './ReviewDetail.vue'
// import CommentList from "@/views/review/CommentList"

export default {
  components: {
    ReviewUpdate,
    ReviewCreate,
  },
  data() {
    return {
      reviewList: "",
      flag1: false,
      reviewid: "",
      commentData: {
        content: "",
      },
      updatecommentData: {
        content: "",
      },
      commentList: "",
      flag: true,
      user:'',
      // 댓글달려고 바꿔주는 형식
      isComment:false,
      commentid:''
    };
  },
  methods: {
    foldReview() {
      this.flag1 = !this.flag1
    },
    login_check(){
      if (this.$cookies.isKey('auth-token')){
        this.user = this.$cookies.get("email")
      }
    },
    getReviewList() {
      axios
        .get(
          constants.SERVER_URL +
            `/reviews/${this.$route.params.movie_pk}/review-list/`
        )
        .then((res) => {
          this.reviewList = res.data;
          this.reviewList = this.reviewList.sort(function(a,b){
          this.flag1=true
          return b.id - a.id;
          })
          })
          .catch((err) => {
          console.log(err.response.data);
        });
    },
    deleteReview(id) {
      Swal.fire({
        text: "후기를 삭제하시겠습니까?",
        width:400,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: '<span style="font-weight:bold;">삭제</span>',
        cancelButtonText:'<span style="font-weight:bold;">취소</span>'
      }).then((result) => {
        if (result.isConfirmed) {
          const Toast = Swal.mixin({
            toast: true,
            position: 'top-end',
            showConfirmButton: false,
            timer: 3000,
            timerProgressBar: true,
          })

          Toast.fire({
            icon: 'success',
            title: '후기가 삭제되었습니다!'
          })
          axios.delete(constants.SERVER_URL + `/reviews/${id}/delete-review/`)
            .then(() => {
              this.getReviewList();
            }).catch((err) => {
            console.log(err.response.data);
            });
          }
      })
      
    },
    goUpdatePage(id) {
      this.$router
        .push({ name: "ReviewUpdate", params: { review_pk: id } })
        .catch(() => {
          this.$router.go();
        });
    },
    goCreateReview() {
      this.$router
        .push({
          name: "ReviewCreate",
          params: { movie_pk: this.$route.params.movie_pk },
        })
        .catch(() => {
          this.$router.go();
        });
    },
    goReviewDetail(id) {
      this.$router
        .push({ name: "ReviewDetail", params: { review_pk: id } })
        .catch(() => {
          this.$router.go();
        });
    },
    getReviewDetail1(id) {
      this.reviewid = id;
      if (this.flag1 == false) {
        this.flag1 = true;
      }else{
        this.flag1 = false
      }
      axios
      .get(
        constants.SERVER_URL +
          `/reviews/${id}/comment-list/`
      )
      .then((res) => {
        this.commentList = res.data;
        this.commentList = this.commentList.sort(function(a,b){
          return b.id- a.id;
        })
      })
      .catch((err) => {
        console.log(err);
      });
    },
  // 댓글 리스트
  getCommentList(id) {
    axios
      .get(
        constants.SERVER_URL +
          `/reviews/${id}/comment-list/`
      )
      .then((res) => {
        this.commentList = res.data;
        this.commentList = this.commentList.sort(function(a,b){
          return b.id- a.id;
        })
      })
      .catch((err) => {
        console.log(err);
      });
  },
  createComment(id) {
    const config = {
      headers: {
        Authorization: `Token ${this.$cookies.get("auth-token")}`,
      },
    };
    axios
      .post(
        constants.SERVER_URL +
          `/reviews/${id}/create-comment/`,
        this.commentData,
        config
      )
      .then((res) => {
        console.log(res)
        this.getReviewDetail1(id)
        this.getCommentList(id)
        this.commentData.content = ''
      })
      .catch((err) => {
        console.log(err.response.data);
      });
  },
  updateComment(commentid, reviewid) {
    const config = {
      headers: {
        Authorization: `Token ${this.$cookies.get("auth-token")}`,
      },
    };
    axios
      .post(
        constants.SERVER_URL + `/reviews/${commentid}/update-comment/`,
        this.updatecommentData,
        config
      )
      .then(() => {
        this.getCommentList(reviewid)
        this.isComment = false
      })
      .catch((err) => {
        console.log(err.response.data);
      });
  },
  deleteComment(id) {
    axios
      .delete(constants.SERVER_URL + `/reviews/${id}/delete-comment/`)
      .then(() => {
      })
      .catch((err) => {
        console.log(err);
      });
  },
  isCommentUpdate(commentid,content){
    this.commentid = commentid
    this.isComment = true
    this.updatecommentData.content = content
  },
  },
  created() {
    this.login_check()
    this.getReviewList();
    // this.getCommentList();
  },
};
</script>

<style>
</style>