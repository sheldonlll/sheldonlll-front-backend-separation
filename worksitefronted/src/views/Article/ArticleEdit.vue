<template>
	<v-container v-if="articledata">
		<v-row>
			<h1>编辑文章</h1>
			<p>{{articledata.body}}</p>
			<v-img :src="articledata.cover"></v-img>
		</v-row>
	</v-container>
</template>

<script>
	import {getarticledetail} from '@/network/Article/netArticle.js'
	export default{
		data(){
			return{
				senddata:null,
				articledata:null,
				ContentType:null,
				ObjectId:null,
			}
		},
		mounted() {
			this.getarticle()
		},
		methods:{
			getarticle(){
				getarticledetail(this.$route.params.id).then(res=>{
					this.articledata = res.data
				}).catch(err=>{
					console.log(err)
				})
			}
		}
	}
</script>

<style scoped="scoped">
</style>
