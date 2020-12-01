<template>
  <div>
    <div
      class="modal fade"
      id="Update"
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
              style="font-weigth: bold; font-size: 1.8rem; margin-left: 15%"
            >
              🆄🅿🅳🅰🆃🅴
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
          <div class="p-5">
            <!-- img upload -->
            <div class="form-group">
              <label class="d-flex">
                <i class="fas fa-images"
                  style="color:white;"
                  ><span class="ml-1">Profile Img</span></i
                >
              </label>
              <div
                class="card"
                style="
                  width: 20rem;
                  height: 20rem;
                  border-radius: 15px;
                  margin-left: 2px;
                "
              >
                <img
                  v-if="profileData.profile_image"
                  :src="profileData.profile_image"
                  class="card-img-top d-flex"
                  style="width: 20rem; height: 20rem; border-radius: 15px; position:relative;"
                  aling-left
                />
                <!-- <div class="card-body">
                        <h5 class="card-title">Card title</h5>
                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                        <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div> -->
              </div>
              <input
                ref="imageInput"
                type="file"
                hidden
                @change="onChangeImages"
              />

              <button
                class="btn btn-default btn-sm mt-2 d-flex inline"
                style="
                  border: 1.5px solid #2ec4b6;
                  border-radius: 15px;
                  font-weight: bold;
                "
                type="button"
                @click="onClickImageUpload"
              >
                <span class="my-auto mr-1" style="color:white;">이미지 업로드</span>
                <div class="mb-1">
                  <small style="font-weight: bold; color:white;">(1MB 이하)</small>
                </div>
              </button>
            </div>

            <!-- 닉네임 입력칸 -->
            <div class="form-group">
              <label for="exampleInputPassword1" class="d-flex">
                <i class="fas fa-smile" style="color:white;"><span class="ml-1">Nickname</span></i>
              </label>
              <input
                v-model="profileData.username"
                type="text"
                class="form-control"
                id="nickname"
              />
              <small
                id="emailHelp"
                class="form-text text-muted d-flex"
                v-if="!error.nickname"
                >닉네임을 입력하세요.</small
              >
              <span
                class="error-text d-flex mt-1"
                v-if="error.nickname"
                style="color: crimson"
                >{{ error.nickname }}</span
              >
            </div>

            <!-- 비밀번호 입력칸 -->
            <div class="form-group">
              <label for="exampleInputPassword1" class="d-flex">
                <i class="fas fa-eye" style="color:white;"><span class="ml-1">Password</span></i>
              </label>
              <input
                v-model="profileData.password"
                :type="passwordType"
                class="form-control"
                id="password"
              />
              <small
                id="emailHelp"
                class="form-text text-muted d-flex"
                v-if="!error.password"
                >비밀번호를 입력하세요.</small
              >
              <span :class="{ active: passwordType === 'text' }">
                <span
                  class="error-text d-flex mt-1"
                  v-if="error.password"
                  style="color: crimson"
                  >{{ error.password }}</span
                >
              </span>
            </div>
            <div style="margin-left: 10%; margin-right: 10%">
              <hr />
            </div>

            <!-- 수정 -->
            <div
              @click="update"
              data-dismiss="modal"
              class="mt-2 row"
              style="cursor: pointer; margin-left: 0%; margin-right: 0%"
            >
              <div
                class="col-12 d-flex justify-content-center align-items-center"
                style="
                  border: 2px solid #2ec4b6;
                  height: 2rem;
                  border-radius: 5px;
                "
              >
                <i class="fas fa-sign-in-alt" style="color:white;"></i
                ><span class="ml-2" style="font-weight: bold; color:white;"
                  >회원 정보 수정</span
                >
              </div>
            </div>

            <div class="mt-2" style="margin-left: 10%; margin-right: 10%">
              <hr />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import PV from "password-validator";
// import * as EmailValidator from "email-validator";
import axios from "axios";
import constants from "../../lib/constants";
import Swal from "sweetalert2";

export default {
  data: function () {
    return {
      file: "",
      profileData: {
        email: "",
        username: "",
        profile_image: "",
        password: "",
      },
      passwordSchema: new PV(),
      error: {
        nickname: false,
        password: false,
      },
      passwordType: "password",
    };
  },
  created() {
    this.getProfileData();
    this.passwordSchema
      .is()
      .min(8)
      .is()
      .max(100)
      .has()
      .digits()
      .has()
      .letters();
  },
  watch: {},
  methods: {
    join() {
      this.$router.push("/user/join");
    },
    onClickImageUpload() {
      this.$refs.imageInput.click();
    },
    onChangeImages(e) {
      this.file = e.target.files[0];
      if (this.file == null) {
        return;
      }
      if (this.file.size >= 1048576) {
        const Toast = Swal.mixin({
          toast: true,
          position: "top-end",
          showConfirmButton: false,
          timer: 2000,
          timerProgressBar: true,
          onOpen: (toast) => {
            toast.addEventListener("mouseenter", Swal.stopTimer);
            toast.addEventListener("mouseleave", Swal.resumeTimer);
          },
        });

        Toast.fire({
          icon: "error",
          title: "파일 업로드 크기를 초과하였습니다!",
        });
        return;
      }
      this.profileData.profile_image = URL.createObjectURL(this.file);
    },
    getProfileData() {
      if (this.$cookies.isKey("auth-token")) {
        const config = {
          headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
        }
        axios
          .get(
            `${constants.SERVER_URL}/accounts/userdetail/`,config
          )
          .then((res) => {
            this.profileData.profile_image = res.data.user_data.profile_image;
            this.profileData.username = res.data.user_data.username;
            this.profileData.email = res.data.user_data.email;
          })
          .catch((err) => {
            console.log(err);
          });
      } else {
        this.$router.push({ name: constants.URL_TYPE.MAIN });
      }
    },
    update() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      if (!this.profileData.username || !this.profileData.password) {
        const Toast = Swal.mixin({
          toast: true,
          position: 'top-end',
          showConfirmButton: false,
          timer: 3000,
          timerProgressBar: true,
        })

        Toast.fire({
          icon: 'error',
          title: '수정할 정보를 입력해주세요!'
        })
        return
      } else {
        axios.post(`${constants.SERVER_URL}/accounts/update-user/${this.profileData.email}/`,this.profileData,config)
          .then(() => {
            this.getProfileData();
            const Toast = Swal.mixin({
              toast: true,
              position: 'top-end',
              showConfirmButton: false,
              timer: 1200,
              timerProgressBar: true,
            })
            Toast.fire({
              icon: 'success',
              title: '회원 정보 수정 완료!'
            })
            setTimeout(() => {
              this.$router.go()
            },1200)
          })
          .catch((err) => {
            console.log(err.data);
          });
      }
    },
  },
};
</script>

<style>
</style>
