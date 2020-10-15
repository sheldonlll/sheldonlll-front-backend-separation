<template>
	<nav>
		<v-app-bar flat app color="rgba(189,189,189,0.6)">
			<!-- 展开栏 -->
			<v-app-bar-nav-icon class="grey--text" @click="drawer = !drawer"></v-app-bar-nav-icon>
			
			<!-- LOGO -->
			<v-toolbar-title class="text-uppercase grey--text font-weight-bold" @click="NavClick('Home')">
				<span class="font-weight-light orange--text text-h4">article</span>
				<span class="text-h4">me</span>
			</v-toolbar-title>
			
			<!-- 左右分布 -->
			<v-spacer></v-spacer>
			
			<!-- 搜索框 -->
			<v-text-field solo-inverted flat hide-details clearable label="Search" prepend-inner-icon="search" class="search"></v-text-field>
			
			<!-- 退出登陆 -->
			<v-btn text class="grey lighten-5" large @click="NavClick('LogOut')" v-if="this.$store.state.islogin && islogin">
				<span>Log Out</span>
			</v-btn>
			
			<!-- 登陆 -->
			<v-btn text class="grey lighten-5" large @click="NavClick('Login')" v-if="!this.$store.state.islogin || !islogin">
				<span>Login In</span>
			</v-btn>
			
			<!-- 注册 -->
			<v-btn text class="grey lighten-5" large @click="NavClick('SignUp')" v-if="!this.$store.state.islogin || !islogin">
				<span>Sign Up</span>
			</v-btn>
			
		</v-app-bar>
		
		<!-- 栏展开 -->
		<v-navigation-drawer v-model="drawer" app class="grey lighten-5" temporary>
			<v-list-item-group v-model="group" active-class="deep-purple--text text--accent-4">
			  <v-list-item two-line :class="miniVariant && 'px-0'" @click="NavClick('Profile')">
				  <v-list-item-avatar>
					<!-- <v-lazy> -->
						<v-img :src="userinfo.avatar||''">
						</v-img>
					<!-- </v-lazy> -->
				  </v-list-item-avatar>
	  
				  <v-list-item-content>
					<v-list-item-title>{{userinfo.username}}</v-list-item-title>
					<v-list-item-subtitle>{{userinfo.personalsignature}}</v-list-item-subtitle>
				  </v-list-item-content>
				</v-list-item>
			  
			  <v-list-item @click="NavClick('Home')">
				<v-list-item-title>主页</v-list-item-title>
			  </v-list-item>
			  
			  <v-list-item @click="NavClick('ArticleList')">
			  	<v-list-item-title>文章</v-list-item-title>
			  </v-list-item>
			  
			  <v-list-item @click="NavClick('MusicList')">
				<v-list-item-title>音乐</v-list-item-title>
			  </v-list-item>
			  
			  <v-list-item @click="NavClick('VideoList')">
			  	<v-list-item-title>影视</v-list-item-title>
			  </v-list-item>
			  
			  <v-list-item @click="NavClick('Chat')">
			  	<v-list-item-title>聊天室</v-list-item-title>
			  </v-list-item>
	
			  <v-list-item @click="NavClick('Profile')">
				<v-list-item-title>个人中心</v-list-item-title>
			  </v-list-item>
			  
			  <v-list-item @click="NavClick('Settings')">
				<v-list-item-title>系统设置</v-list-item-title>
			  </v-list-item>
			  
			  <v-list-item @click="NavClick('FeedBack')">
			  	<v-list-item-title>反馈</v-list-item-title>
			  </v-list-item>
	
			</v-list-item-group>
		  </v-list>
		</v-navigation-drawer>
	</nav>
</template>

<script>
	import {getuserinfo} from '@/network/Profile/netProfile.js'
	export default{
		data(){
			return{
				drawer: false,
				group: null,	
				miniVariant: false,
				islogin: false,
				userinfo:{
					avatar:null,
					username:null,
					personalsignature:null
				}
			}
		},
		inject: ['reload'], //注入，局部刷新
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
		watch: {
		  group () {
			this.drawer = false
		  },
		  '$route.path'(val,oldVal){
			  if(val=='/home'){
				  this.getUserInfo()
			  }
		  }
		},

		methods:{
			// 路由跳转
			NavClick(path){
				if(path=='LogOut'){
					this.$store.commit('logoutOK')
					this.getUserInfo()
					this.reload() //局部刷新
					return;
				}
				this.$router.push({name: path})
			},
			getUserInfo(){
				if(localStorage.getItem('userid')){
					this.islogin = true
					getuserinfo(localStorage.getItem('userid')).then(res => {
						this.userinfo.avatar = res.data.avatar
						this.userinfo.username = res.data.account_username
						this.userinfo.personalsignature = res.data.personalsignature
						console.log(this.userinfo,'user')
						this.reload() //局部刷新
					}).catch(err => {
						console.log(err)
					})
				}else{
					this.islogin = false
					this.avatar =  "https://randomuser.me/api/portraits/men/83.jpg"
				}
			}
		}
	}
</script>

<style scoped="scoped">
	.search{
		width: 0.1%;
	}
</style>
