<template>
  <div class="container col-10 col-md-8" style="aling:center">
    <div class="mt-4 mb-4">
        <i class="far fa-address-card" style="font-size:30px;"><span class="ml-2">회원 가입</span></i>
    </div>

    <div class="row">
        <div class="col-12 col-sm-8 col-md-6 col-lg-6 col-xl-6">
            <!-- img upload -->
            <div class="form-group">
                <label class="d-flex">
                    <i class="fas fa-images"><span class="ml-1">Profile Img</span></i>
                </label>
                <div class="card" style="width:20rem; height:20rem; border-radius:15px; margin-left:2px">
                    <img v-if="pro_img" :src="pro_img" class="card-img-top d-flex" style="width: 20rem; height:20rem; border-radius:15px;" aling-left>
                    <!-- <div class="card-body">
                        <h5 class="card-title">Card title</h5>
                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                        <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div> -->
                </div>
                <input ref="imageInput" type="file" hidden @change="onChangeImages">
                
                <button class="btn btn-default btn-sm mt-2 d-flex inline" style="border:1.5px solid #2EC4B6; border-radius:15px; font-weight:bold;" type="button" @click="onClickImageUpload"><span class="my-auto mr-1">이미지 업로드</span><div class="mb-1"><small style="font-weight:bold">(1MB 이하)</small></div></button>
            </div>
        </div>
        
        <div class="col-12 col-sm-4 col-md-6 col-lg-6 col-xl-6">

            <!-- 닉네임 입력칸 -->
            <div class="form-group">
                <label for="exampleInputPassword1" class="d-flex">
                    <i class="fas fa-smile"><span class="ml-1">Nickname</span></i>
                </label>
                <input
                    v-model="nickname"
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
                    style="color:crimson;"
                    >{{ error.nickname }}</span
                >
            </div>

            <!-- email 입력칸 -->
            <div class="form-group">
                <label for="exampleInputPassword1" class="d-flex">
                    <i class="fas fa-at"><span class="ml-1">E-mail</span></i>
                </label>
                <input
                    v-model="email"
                    type="text"
                    class="form-control"
                    id="email"
                />
                <small
                    id="emailHelp"
                    class="form-text text-muted d-flex"
                    v-if="!error.email"
                    >이메일을 입력하세요.</small
                >
                <span
                    class="error-text d-flex mt-1"
                    v-if="error.email"
                    style="color:crimson;"
                    >{{ error.email }}</span
                >
            </div>

            <!-- 비밀번호 입력칸 -->
            <div class="form-group">
                <label for="exampleInputPassword1" class="d-flex">
                    <i class="fas fa-eye"><span class="ml-1">Password</span></i>
                </label>
            <input
                v-model="password"
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
                    style="color:crimson;"
                    >{{ error.password }}</span
                    >
                </span>
            </div>

            <!-- 비밀번호 확인 입력칸 -->
            <div class="form-group">
                <label for="exampleInputPassword1" class="d-flex">
                    <i class="fas fa-eye"><span class="ml-1">Password Confirm</span></i>
                </label>
                <input
                    v-model="passwordconfirm"
                    :type="passwordConfirmType"
                    class="form-control"
                    id="passwordconfirm"
                />
                <small
                    id="emailHelp"
                    class="form-text text-muted d-flex"
                    v-if="!error.passwordconfirm"
                    >비밀번호를 다시 입력하세요.</small
                >
                <span :class="{ active: passwordConfirmType === 'text' }">
                    <span
                    class="error-text d-flex mt-1"
                    v-if="error.passwordconfirm"
                    style="color:crimson;"
                    >{{ error.passwordconfirm }}</span
                    >
                </span>
            </div>
        </div>
    </div>
    <hr>
    <div class="d-flex justify-content-end">
        <button @click="goMain" class="btn btn-default" style="border:1px solid lightgray; border-radius:15px"><i class="fas fa-home"><span class="ml-2">Main 화면으로</span></i></button>
        <button @click="signup" class="btn btn-default ml-2" style="border:1px solid lightgray; border-radius:15px"><i class="fas fa-user-plus"><span class="ml-2">회원가입</span></i></button>
    </div>


    

    

  </div>
</template>

<script>
import Swal from "sweetalert2";
import axios from 'axios'
import constants from '../../lib/constants'

// const baseURL = process.env.VUE_APP_BACKURL;

export default {
    data() {
        return {
            file: "",
            pro_img: "",
            name: "",
            nickname:"",
            email:"",
            password: "",
            passwordconfirm: "",
            error: {
                email: false,
                name: false,
                password: false,
                nickname: false,
                passwordconfirm: false,
            },
            passwordType: "password",
            passwordConfirmType: "password",
        }
    },
    methods: {
        signup(){
            let signupData = {
                username: this.nickname,
                email:this.email,
                password1:this.password,
                password2:this.passwordconfirm,
            }
            axios.post(constants.SERVER_URL + '/rest-auth/signup/',signupData)
            .then((res)=>{
                console.log(res)
                this.$router.push({name:constants.URL_TYPE.MAIN})
            })
        },
        onClickImageUpload() {
            this.$refs.imageInput.click();
        },
        onChangeImages(e) {
            this.file = e.target.files[0];
            if(this.file == null) {
                return;
            }
            if(this.file.size >= 1048576) {
                const Toast = Swal.mixin({
                toast: true,
                position: 'top-end',
                showConfirmButton: false,
                timer: 2000,
                timerProgressBar: true,
                onOpen: (toast) => {
                    toast.addEventListener('mouseenter', Swal.stopTimer)
                    toast.addEventListener('mouseleave', Swal.resumeTimer)
                }
                })

                Toast.fire({
                icon: 'error',
                title: '파일 업로드 크기를 초과하였습니다!'
                })
                return;
            }
            this.pro_img = URL.createObjectURL(this.file);
        },
        goMain() {
            Swal.fire({
                width:350,
                text: "Home으로 이동시 입력한 정보는 저장되지 않습니다.",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#F5F5F5',
                cancelButtonColor: '#F5F5F5',
                confirmButtonText: '<span style="color:black; font-size:1rem;">yes</span>',
                cancelButtonText: '<span style="color:black; font-size:1rem;">cancel</span>'
                }).then((result) => {
                    if (result.isConfirmed) {
                        this.$router.push('/').catch(() => {
                            this.$router.go()
                        })
                    }
                })
        },
        // join() {
        //     axios.post(`${baseURL}/`)
        // },
    }
}
</script>

<style>

</style>
