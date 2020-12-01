<template>
  <div>
    <div
      class="modal fade"
      id="ReviewCreate"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      role="dialog"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content" style="width: 100%; border: 0">
          <div class="modal-header" style="background-color: #efffe8">
            <h5
              class="modal-title my-auto"
              id="exampleModalLabel"
              style="font-weigth: bold; font-size: 1.8rem; margin-left: 4%; color:Crimson;"
            >
              🆁🅴🆅🅸🅴🆆
            </h5>
            <button
              type="button"
              class="close my-auto"
              data-dismiss="modal"
              aria-label="Close"
            >
              <span aria-hidden="true">&times;</span>
            </button>
          </div>

          <div class="p-3" style="background-color: white">
            <div class="modal-body">
              <div>
                <h5 class="font-weight-bold">제목</h5>
                <input
                  placeholder="제목을 입력해 주세요."
                  type="text"
                  v-model="reviewData.summary"
                  class="mb-4 p-2 w-100 float-left"
                />
              </div>
              <div>
                <h5 class="font-weight-bold">내용</h5>
                <textarea
                  placeholder="내용을 입력해 주세요"
                  style="width: 100%"
                  name=""
                  id=""
                  class="p-2"
                  cols="30"
                  rows="10"
                  v-model="reviewData.content"
                ></textarea>
              </div>
            </div>
            <b-button
              class="float-right m-3"
              @click="createReview"
              data-dismiss="modal"
              ><i class="fas fa-pencil-alt"></i><span class="ml-2">작성 완료</span></b-button
            >
            <input
              class="mx-3"
              type="checkbox"
              id="checkbox"
              v-model="reviewData.spo"
            />
            <label for="checkbox">스포방지</label>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import constants from "../../lib/constants";
import Swal from "sweetalert2";

export default {
  data() {
    return {
      reviewData: {
        movie_id: this.$route.params.movie_pk,
        summary: "",
        content: "",
        spo: false,
      },
    };
  },
  methods: {
    createReview() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      };
      if(!this.reviewData.summary && this.reviewData.content) {
        const Toast = Swal.mixin({
          toast: true,
          position: 'top-end',
          showConfirmButton: false,
          timer: 3000,
          timerProgressBar: true,
        })

        Toast.fire({
          icon: 'warning',
          title: '제목은 빈칸일 수 없습니다.'
        })
        return
      } else if (this.reviewData.summary && !this.reviewData.content) {
        const Toast = Swal.mixin({
          toast: true,
          position: 'top-end',
          showConfirmButton: false,
          timer: 3000,
          timerProgressBar: true,
        })

        Toast.fire({
          icon: 'warning',
          title: '내용은 빈칸일 수 없습니다.'
        })
        return
      } else if (!this.reviewData.summary && !this.reviewData.content){
        const Toast = Swal.mixin({
          toast: true,
          position: 'top-end',
          showConfirmButton: false,
          timer: 3000,
          timerProgressBar: true,
        })

        Toast.fire({
          icon: 'warning',
          title: '제목과 내용은 빈칸일 수 없습니다.'
        })
        return
      } else {
        axios
          .post(
            constants.SERVER_URL + "/reviews/create-review/",
            this.reviewData,
            config
          )
          .then(() => {
            const Toast = Swal.mixin({
              toast: true,
              position: 'top-end',
              showConfirmButton: false,
              timer: 3000,
              timerProgressBar: true,
            })

            Toast.fire({
              icon: 'success',
              title: '후기 작성 완료!'
            })
            this.$emit('reRender')
          })
          .catch((err) => {
            console.log(err.response.data);
          });
      }
    },
  },
};
</script>

<style>
</style>