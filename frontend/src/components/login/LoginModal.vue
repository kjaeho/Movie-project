<template>
  <div>
      <div class="modal fade" id="Login" tabindex="-1" aria-labelledby="exampleModalLabel" role="dialog" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content" style="width:80%; border:0;">
                <div class="modal-header" style="background-color:#EFFFE8">
                    <h5 class="modal-title my-auto" id="exampleModalLabel" style="font-weigth:bold; font-size:1.8rem; margin-left:15%">🅻🅾🅶🅸🅽</h5>
                    <button type="button" class="close my-auto" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div style="background-color:white;">
                <!-- email 입력 칸 -->  
                <div class="modal-body d-flex justify-content-center mt-2">
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



                <!-- password 입력 칸 -->
                <div class="modal-body d-flex justify-content-center pt-1 pb-2">
                    <i class="fas fa-lock my-auto mr-2" style="font-size:25px"></i>
                    <input
                        class="text-center"
                        style="width:60%; height:35px; border-radius:5px; border:1.5px solid;"
                        type="password"
                        v-model="password"
                        placeholder="Input your password"
                        @keypress.enter="login"
                    />
                </div>

                <div style="margin-left:10%; margin-right:10%">
                    <hr />
                </div>

                <!-- 로그인 -->
                <div @click="login"
                    data-dismiss="modal"
                    class="mt-2 row"
                    style="cursor: pointer; margin-left:18%; margin-right:18%;"
                >
                    <div
                        class="col-12 d-flex justify-content-center align-items-center"
                        style="border:2px solid #2EC4B6; height:2rem; border-radius:5px"
                    >
                    <i class="fas fa-sign-in-alt"></i><span class="ml-2" style="font-weight:bold;">로그인</span>
                    </div>
                </div>

                <!-- 회원가입 -->
                <div
                    data-dismiss="modal"
                    data-toggle="modal" 
                    data-target="#JoinModal"
                    class="mt-2 row"
                    style="cursor: pointer; margin-left:18%; margin-right:18%;"
                >
                    <div
                        class="col-12 d-flex justify-content-center align-items-center"
                        style="border:2px solid #2EC4B6; height:2rem; border-radius:5px"
                    >
                        <i class="far fa-user mr-1"></i><span class="ml-2" style="font-weight:bold">회원가입</span>
                    </div>
                </div>

                <!-- 비밀번호 찾기 -->
                <!-- <div
                    data-dismiss="modal"
                    class="mt-2 row"
                    style="cursor: pointer; margin-left:18%; margin-right:18%;"
                    data-toggle="modal"
                    data-target="#findpassword"
                >
                    <div
                        class="col-12 d-flex justify-content-center align-items-center"
                        style="border:2px solid #2EC4B6; height:2rem; border-radius:5px"
                    >
                        <i class="fas fa-unlock">
                        </i>
                        <span class="ml-2" style="font-weight:bold">비밀번호 찾기</span>
                    </div>
                </div> -->

               
                <!-- <div
                    @click="naverLogin"
                    class="mt-2 row d-flex justify-content-center"
                    style="cursor: pointer; margin-left:18%; margin-right:18%;"
                >
                    <div
                        class="col-12 d-flex justify-content-center align-items-center"
                        style="border:2px solid #2EC4B6; height:2rem; border-radius:5px"
                    >
                        <img
                        src="../../assets/img/naver_logo.png"
                        style="width:20px"
                        /><span class="ml-2" style="font-weight:bold"
                        >네이버 로그인</span>
                    </div>
                </div>

                
                <div
                    class="mt-2 row d-flex justify-content-center"
                    style="cursor: pointer; margin-left:18%; margin-right:18%;"
                >
                    <div
                        class="col-12 d-flex justify-content-center align-items-center"
                        style="border:2px solid #2EC4B6; height:2rem; border-radius:5px"
                    >
                        <img
                        src="../../assets/img/google_logo.jpg"
                        style="width:25px"
                        /><span class="ml-1" style="font-weight:bold"
                        >구글 로그인</span
                        >
                    </div>
                </div> -->

                <div class="mt-2" style="margin-left:10%; margin-right:10%;">
                    <hr />
                </div>

                </div>
                <div class="modal-footer border-0" style="background-color:white;"></div>
            </div>
        </div>
    </div>
    </div>
</template>


<script>
import PV from "password-validator";
// import * as EmailValidator from "email-validator";
import axios from "axios";
import constants from '../../lib/constants'
import Swal from "sweetalert2";

export default {
    data: function() {
        return {
            email: "",
            password: "",
            passwordSchema: new PV(),
            error: {
                email: false,
                password: false,
            },
            passwordType: "password",
            isLoggedIn: false,
        }
    },
    created() {
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
    watch: {
        
    },
    methods: {
        // join() {
        //     this.$router.push('/user/join').catch(() => {
        //         this.$router.go()
        //     })
        // },
        login(){
            let loginData ={
                email:this.email,
                password:this.password
            }
            console.log(loginData)
            axios.post(constants.SERVER_URL+'/rest-auth/login/',loginData)
            .then((res)=>{
                this.isLoggedIn = true
                setTimeout(() => {
                    this.$router.go().catch(() => {
                        this.$router.push('/')
                    })
                },1200)
                this.$cookies.set('auth-token',res.data.key)
                this.$cookies.set('email',loginData.email)
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
                    title: '로그인 성공!'
                })
            })
            .catch(()=>{
                const Toast = Swal.mixin({
                    toast: true,
                    position: 'top-end',
                    showConfirmButton: false,
                    timer: 3000,
                    timerProgressBar: true,
                    // didOpen: (toast) => {
                    //     toast.addEventListener('mouseenter', Swal.stopTimer)
                    //     toast.addEventListener('mouseleave', Swal.resumeTimer)
                    // }
                })

                Toast.fire({
                    icon: 'error',
                    title: '이메일 및 비밀번호를 다시 확인해주세요!'
                })
            })
        },
        naverLogin(){
            axios.get(constants.SERVER_URL+'/saccounts/naver/login/')
                .then(()=>{})
                .catch((err)=>{
                    console.log(err)
                })
        },
    },
}
</script>

<style>

</style>
