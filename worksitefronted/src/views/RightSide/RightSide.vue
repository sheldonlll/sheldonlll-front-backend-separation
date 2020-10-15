<template>
	<v-card>
		<!-- 返回按钮 + 弹幕发送 + 弹幕按钮-->
		<v-btn text color="orange" @click="NavClick('Home')">主页Go！</v-btn>
		<v-btn text color="orange" @click="NavClickList">列表Go！</v-btn>
		<v-btn text color="orange" @click="isshowdanmubox">弹幕开关</v-btn>
		<hr>
		<v-container class="danmubox" v-if="isshow">
			<v-row>
				<input type="text">
				<v-spacer></v-spacer>
				<button>发送</button>
			</v-row>
		</v-container>
		<hr v-if="isshow">
		<!-- 弹幕列表 -->
		<BulletScreen :ObjectId="ObjectId" :ContentType ="ContentType" v-if="isshow"></BulletScreen>
		<hr v-if="isshow">
		<!-- 随机推荐 -->
		<Recommend :ObjectId="ObjectId" :ContentType ="ContentType"></Recommend>
	</v-card>
</template>

<script>
	import Recommend from '@/views/Recommend/Recommend.vue'
	import BulletScreen from '@/views/BulletScreen/BulletScreen.vue'
	export default{
		data(){
			return{
				isshow:true,
				isfull:false,
				listUrl:""
			}
		},
		components:{
			Recommend,
			BulletScreen
		},
		props:{
			ObjectId:{
				type:Number,
				default:0
			},
			ContentType:{
				type:Number,
				default:0
			}
		},
		created() {
			let curpath = this.$router.currentRoute.name.toString()
			if(curpath.match("Article")){
				this.listUrl = "ArticleList"
			}else if(curpath.match("Music")){
				this.listUrl = "MusicList"
			}else if(curpath.match("Video")){
				this.listUrl = "VideoList"
			}
		},
		methods:{
			NavClick(path){
				this.$router.push({name:path})
			},
			NavClickList(){
				this.$router.push({name:this.listUrl})
			},
			isshowdanmubox(){
				this.isshow = !this.isshow
			}
		}
	}
</script>

<style scoped="scoped">

</style>
