<template>
	<v-container>
		<v-btn color="orange" depressed>
			分享
		</v-btn>
		<v-btn color="orange" depressed>
			点赞
		</v-btn>
		<v-btn color="orange" depressed v-if="!isowner">
			打赏
		</v-btn>
		<v-btn color="orange" depressed v-if="!isowner">
			收藏
		</v-btn>
		<v-btn color="orange" depressed v-if="isowner" @click='toedit'>
			编辑
		</v-btn>
		<v-btn color="orange" depressed v-if="isowner" @click='todelete'>
			删除
		</v-btn>
		<v-btn color="orange" depressed v-if="isowner" @click='tofullscreen'>
			全屏
		</v-btn>
	</v-container>
</template>

<script>
	export default{
		data(){
			return{
				isowner:false,
				editUrl:'',
				alert: false,
			}
		},
		props:{
			detaildata:null,
			detailauthorid:0
		},
		mounted() {
			let curpath = this.$router.currentRoute.name.toString()
			if(curpath.match("Article")){
				this.editUrl = "ArticleEdit"
			}else if(curpath.match("Music")){
				// this.editUrl = "MusicList"
			}else if(curpath.match("Video")){
				// this.editUrl = "VideoList"
			}
			let curuserid = localStorage.getItem('userid')
			if(curuserid && curuserid == this.detailauthorid){
				this.isowner = true
			}
		},
		methods:{
			toedit(){
				console.log(this.$route.params.id)
				this.$router.push({name:this.editUrl,params:this.$route.params.id})
			},
			todelete(){
				this.alert = !this.alert
			},
			tofullscreen(){
				this.$emit("tofullscreen")
			}
		}
	}
</script>

<style>
</style>
