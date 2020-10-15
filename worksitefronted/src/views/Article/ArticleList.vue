<template>
	<v-container>
		<!-- 顶部排序 -->
		<v-row dense>
			<v-btn text large>
				<v-icon large>folder</v-icon>
				<span class="caption text-lowercase">By Folder</span>
			</v-btn>
			<v-btn text large>
				<v-icon large>person</v-icon>
				<span class="caption text-lowercase">By Person</span>
			</v-btn>
			<v-btn text large>
				<v-icon large>date_range</v-icon>
				<span class="caption text-lowercase">By Date</span>
			</v-btn>
			<v-spacer></v-spacer>
			<v-btn text large @click="newarticle">
				<v-icon large>create</v-icon>
				<span class="caption text-lowercase">Create</span>
			</v-btn>
		</v-row>
		

		<!-- 列表 -->
		<v-row dense>
		  <v-col v-for="(article,index) in articles" :key="index" :cols="article.flex">
			  <v-card>
					<div @click="showdetail(article.article_id)">
				<v-lazy>
					<v-img class="white--text align-end" height="200px" :src="article.cover">
					  <v-card-title>{{article.title}}</v-card-title>
					</v-img>
				</v-lazy>
			    <v-card-subtitle class="pb-0">{{article.share_at | dateFormat}} {{article.article_author}}</v-card-subtitle>
			    <v-card-text class="text--primary">
			      <div>{{article.body | cutwords}}</div>
			    </v-card-text>
					</div>
			  </v-card>
		  </v-col>
		</v-row>
	</v-container>
</template>

<script>
	import {getarticlelist} from '@/network/Article/netArticle.js'
	export default {
		data: () => ({
			articles:null
		}),
		created(){
			getarticlelist().then(res=>{
				this.articles = res.data.results
				this.articles.sort((a,b)=>{return a.flex > b.flex ? -1:1})
			}).catch(err => {
				console.log(err)
			})
			// 整理布局
		},
		methods:{
			showdetail(id){
				this.$router.push({ name: 'ArticleDetail', params: { id }})
			},
			newarticle(){
				if(!localStorage.getItem('refresh')){
					alert('请先登陆吧')
				}
				else
				{
					this.$router.push({ name: 'NewArticle' })	
				}
			}
		}
	}
</script>

<style>

</style>
