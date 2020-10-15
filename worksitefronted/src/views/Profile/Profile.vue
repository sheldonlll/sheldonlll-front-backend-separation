<template>
	<v-container>
	    <v-row><h1>{{msg}}</h1></v-row>
		<v-row v-if="islogin">
			<v-row>
				<v-col cols="12">
					<v-card color="basil" class="mycardtop">
						<v-card-title class="text-center justify-center py-6">
						  <h1 class="font-weight-bold display-3 basil--text">
							  <v-list-item-avatar>
								<v-img :src="userinfo.avatar||''">
								</v-img>
							  </v-list-item-avatar>
							  <v-list-item-content>
								<v-list-item-title>{{userinfo.username}}</v-list-item-title>
								<v-list-item-subtitle>{{userinfo.personalsignature}}</v-list-item-subtitle>
							  </v-list-item-content>
						  </h1>
						</v-card-title>
					</v-card>
					<v-card color="basil" class="mycardcenter">
						<v-tabs background-color="transparent" color="basil" grow class="mytabs">
						  <v-tab @click="tabnotshowside" class="mytab">
							<span>主页</span>
						  </v-tab>
						  <v-tab @click="tabnotshowside" class="mytab" flat>
							<span>动态</span>
						  </v-tab>
						  <v-tab @click="tabtoshowside" class="mytab">
							<span>收藏</span>
						  </v-tab>
						  <v-tab @click="tabtoshowside" class="mytab">
							<span>消息</span>
						  </v-tab>
						</v-tabs>
					</v-card>
					<v-card>
						{{text}}
					</v-card>
				</v-col>
			</v-row>
		</v-row>
	</v-container>
</template>

<script>
	import {getuserinfo} from '@/network/Profile/netProfile.js'
	export default{
		data(){
			return{
				islogin:false,
				tabcols:12,
				sidecols:0,
				msg:"",
				userinfo:{
					avatar:null,
					username:null,
					personalsignature:null
				},
				text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
					
			}
		},
		mounted(){
			if(localStorage.getItem('userid')){
				this.islogin = true
				getuserinfo(localStorage.getItem('userid')).then(res => {
					this.userinfo.avatar = res.data.avatar
					this.userinfo.username = res.data.account_username
					this.userinfo.personalsignature = res.data.personalsignature
					this.reload() //局部刷新
				}).catch(err => {
					console.log(err)
				})
			}else{
				this.islogin = false
				this.avatar =  "https://randomuser.me/api/portraits/men/83.jpg"
			}
		},
		methods:{
			tabtoshowside(){
				this.tabcols = 11
				this.sidecols = 1
			},
			tabnotshowside(){
				this.tabcols = 12
				this.sidecols = 0
			}
		}
	}
</script>

<style scoped="scoped">
	.basil {
	  background-color: #FFFBE6 !important;
	}
	.basil--text {
	  color: #356859 !important;
	}
	.mycardcenter{
		border-radius: 0;
	}
	.mycardtop{
		border-radius: 0;
		border: 1px solid #CCCCCC;
	}
</style>
