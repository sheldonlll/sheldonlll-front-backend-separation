<template>
	<v-container>
	    <v-row>
			<v-col :cols="mainpartcols" class="leftpart">
				<!-- 具体文章 -->
				<v-card class="articlepart">
					<div class="cover">
					<v-lazy>
					<v-img class="black--text align-end" height="500px" :src="articledata.cover">
					  <v-card-title class="articeltitle">{{articledata.title}}</v-card-title>
					</v-img>
					</v-lazy>
					</div>
					<v-card-subtitle class="pb-0">{{articledata.share_at}} {{articledata.upddate_at}} {{articledata.article_author}} {{articledata.type}}</v-card-subtitle>
					<v-card-text class="text--primary">
					  <div class="articlebody">{{articledata.body}}</div>
					</v-card-text>
						
					<!-- 点赞分享等按钮 -->
					<v-card-actions>
					  <ToolOps  @tofullscreen="tofullscreen" :detaildata="articledata" :detailauthorid="articledata.article_author_id" v-if="articledata && articledata.article_author_id"></ToolOps>
					</v-card-actions>
				</v-card>
				<!-- 该文章对应评论 -->
				<v-card class="commentpart">
					<Comment :ContentType = "ContentType" :ObjectId = "ObjectId" v-if ="ContentType && ObjectId"></Comment>
				</v-card>
			</v-col>
			<!-- 右侧推荐及弹幕列表等 -->
			<v-col :cols="sidepartcols" class="rightpart">
				<RightSide :ObjectId ="ObjectId" :ContentType ="ContentType" v-if ="ContentType && ObjectId"></RightSide>
			</v-col>
		</v-row>
	</v-container>
</template>

<script>
	import {getarticledetail} from '@/network/Article/netArticle.js'
	import Comment from '@/views/Comment/Comment.vue'
	import RightSide from '@/views/RightSide/RightSide.vue'
	import ToolOps from '@/views/ToolOps/ToolOps.vue'
	export default{
		name:'ArticleDetail',
		data(){
			return{
				articledata:{
					pic:"https://images.app.goo.gl/gw7YT4RndTV6d9tz8"
				},
				canEdit:false,
				ContentType:null,
				ObjectId:null,
				mainpartcols:8,
				sidepartcols:4,
				fullclickcnt:0
			}
		},
		components:{
			Comment,
			RightSide,
			ToolOps
		},
		created() {
			getarticledetail(this.$route.params.id).then(res=>{
				this.articledata = res.data
				this.ContentType = this.articledata.get_content_type
				this.ObjectId = parseInt(this.$route.params.id)

			}).catch(err => {
				console.log(err)
			})
		},
		methods:{
			tofullscreen(){
				if(this.fullclickcnt){
					this.mainpartcols = 8
					this.sidepartcols = 4
					this.fullclickcnt = 0
				}else{
					this.fullclickcnt = 1
					this.mainpartcols = 12
					this.sidepartcols = 12
				}
				
			}
		}
		
	}
</script>

<style scoped="scoped">
	.articeltitle{
		color: #8F3F71;
	}
	.articlebody{
		text-indent:2em;
	}
	.articlepart{
		margin-bottom: 5px;
		border: 1px solid silver;
	}
	.commentpart{
		margin-top: 5px;
		border: 1px solid gold;
	}

</style>
