<template>
  <div>
    <div class="modal fade" id="JoinModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content" style="width:80%; border:0;">
                <div class="modal-header" style="background-color:#EFFFE8">
                    <h5 class="modal-title my-auto" id="exampleModalLabel" style="font-weight:bold; font-size:1.8rem; margin-left:15%">🆂🅸🅶🅽 🆄🅿</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div style="background-color:white;">
                <!-- username 입력 칸 -->
                <div class="modal-body d-flex justify-content-center pb-0">
                    <i
                        v-if="!error.username"
                        class="fas fa-file-signature my-auto mr-1"
                        style="font-size:25px"
                    ></i>
                    <i
                        v-if="error.username"
                        class="fas fa-file-signature my-auto mr-1"
                        style="font-size:25px; color:red"
                        title="이메일 형식이 아닙니다!"
                    ></i>
                    <input
                        class="text-center"
                        style="width:60%; height:35px; border-radius:5px;border:1.5px solid;"
                        type="text"
                        v-model="username"
                        placeholder="input your username."
                    />
                </div>
                <small v-if="!error.username" class="d-flex justify-content-end" style="width:82%; margin-bottom:1rem; font-weight:bold; padding-left:27%">닉네임을 입력해주세요!</small>
                <small v-if="error.username" class="d-flex justify-content-end" style="width:82%; margin-bottom:1rem; font-weight:bold; color:red; padding-left:27%">{{error.username}}</small>

                
                <!-- email 입력 칸 -->
                <div class="modal-body d-flex justify-content-center pt-0 pb-0">
                    <i
                        v-if="!error.email"
                        class="fas fa-envelope my-auto mr-2"
                        style="font-size:25px"
                    ></i>
                    <i
                        v-if="error.email"
                        class="fas fa-envelope my-auto mr-2"
                        style="font-size:25px; color:red"
                        title="이메일 형식이 아닙니다!"
                    ></i>
                    <input
                        class="text-center"
                        style="width:60%; height:35px; border-radius:5px;border:1.5px solid;"
                        type="text"
                        v-model="email"
                        placeholder="email@example.com"
                    />
                </div>
                <small v-if="!error.email" class="d-flex justify-content-end" style="width:82%; margin-bottom:1rem; font-weight:bold; padding-left:27%">이메일을 입력해주세요!</small>
                <small v-if="error.email" class="d-flex justify-content-end" style="width:82%; margin-bottom:1rem; font-weight:bold; color:red; padding-left:27%">{{error.email}}</small>

                <!-- password 입력 칸 -->
                <div class="modal-body d-flex justify-content-center pt-0 pb-0">
                    <i
                        v-if="!error.password"
                        class="fas fa-key my-auto mr-2"
                        style="font-size:25px"
                    ></i>
                    <i
                        v-if="error.password"
                        class="fas fa-key my-auto mr-2"
                        style="font-size:25px; color:red"
                        title="비밀번호 형식이 다릅니다!"
                    ></i>
                    <input
                        class="text-center"
                        style="width:60%; height:35px; border-radius:5px;border:1.5px solid;"
                        type="password"
                        v-model="password"
                        placeholder="특수문자를 포함한 8자 이상"
                    />
                </div>
                <small v-if="!error.password" class="d-flex justify-content-end" style="width:82%; margin-bottom:1rem; font-weight:bold; padding-left:27%">비밀번호를 입력해주세요!</small>
                <small v-if="error.password" class="d-flex justify-content-end" style="width:82%; margin-bottom:1rem; font-weight:bold; color:red; padding-left:27%">{{error.password}}</small>
                
                <!-- passwordConfirm 입력 칸 -->
                <div class="modal-body d-flex justify-content-center pt-0 pb-0">
                    <i
                        v-if="!error.passwordconfirm"
                        class="fas fa-check-circle my-auto mr-2"
                        style="font-size:25px"
                    ></i>
                    <i
                        v-if="error.passwordconfirm"
                        class="fas fa-check-circle my-auto mr-2"
                        style="font-size:25px; color:red"
                        title="비밀번호가 동일하지 않습니다!"
                    ></i>
                    <input
                        class="text-center"
                        style="width:60%; height:35px; border-radius:5px;border:1.5px solid;"
                        type="password"
                        v-model="passwordconfirm"
                        placeholder="password Check"
                    />
                </div>
                <small v-if="!error.passwordconfirm" class="d-flex justify-content-end" style="width:82%; margin-bottom:1rem; font-weight:bold; padding-left:27%">비밀번호를 확인해주세요!</small>
                <small v-if="error.passwordconfirm" class="d-flex justify-content-end" style="width:82%; margin-bottom:1rem; font-weight:bold; color:red; padding-left:27%">{{error.passwordconfirm}}</small>
                </div>

                <div class="modal-footer" style="background-color:white;">
                    <button type="button" class="btn btn-default btn-sm" style="border:2px black solid; border-radius:10px" data-dismiss="modal"><i class="far fa-window-close"><span class="ml-2" style="font-weight:bold">Close</span></i></button>
                    <button @click="signup" type="button" class="btn btn-default btn-sm" style="border:2px black solid; border-radius:10px; margin-right:15%"><i class="fas fa-user-plus"><span class="ml-2">회원 가입</span></i></button>
                </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import Swal from "sweetalert2";
import axios from 'axios'
import constants from '../../lib/constants'

export default {
    data() {
        return {
            username:"",
            email:"",
            password: "",
            passwordconfirm: "",
            error: {
                username: false,
                email: false,
                password: false,
                passwordconfirm: false,
            },
            passwordType: "password",
            passwordConfirmType: "password",
        }
    },
    methods: {
        signup() {
            let signupData = {
                username: this.username,
                email: this.email ,
                password1: this.password,
                password2: this.passwordconfirm,
            }
            axios.post(`${constants.SERVER_URL}/rest-auth/signup/`,signupData)
                .then(() => {
                    const Toast = Swal.mixin({
                        toast: true,
                        position: 'top-end',
                        showConfirmButton: false,
                        timer: 1000,
                        timerProgressBar: true,
                        // didOpen: (toast) => {
                        //     toast.addEventListener('mouseenter', Swal.stopTimer)
                        //     toast.addEventListener('mouseleave', Swal.resumeTimer)
                        // }
                    })

                    Toast.fire({
                        icon: 'success',
                        title: '회원가입을 축하합니다!'
                    })
                    setTimeout(() => {
                        this.$router.go()
                    },1200)
                }).catch((err) => {
                    if (err.response.data.email) {
                        this.error.email = err.response.data.email[0]
                    }
                    if (err.response.data.username) {
                        this.error.username = err.response.data.username[0]
                    }
                    if (this.email.length < 8) {
                        this.error.password = '비밀번호가 너무 짧습니다.'
                    } else if (err.response.data.password1) {
                        this.error.password = err.response.data.password1[0]
                        }
                    if (err.response.data.non_field_errors) {
                        this.error.passwordconfirm = err.response.data.non_field_errors[0]
                    }
                    // this.error.email = err.response.data.email
                })
        },
    },
}
</script>

<style>

</style>