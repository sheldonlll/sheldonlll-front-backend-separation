<template>
	<div>
		<v-row v-for="(comment,index) in commentsobj.replies||[]" class="commentlayer" v-if="comment.replies">
			<v-col cols='1' class="commentlayerleft">
				<v-list-item-avatar class="commentavatar">
					<v-img :src="comment.author_avatar">
					</v-img>
				</v-list-item-avatar>
			</v-col>
			<v-col cols='11' class="commentlayerright">
				<div class="commentlayerup">
					<div>{{comment.comment_author}} <span>:</span> {{comment.create_at | dateFormat}}</div>
				</div>
				<hr>
				<div class="commentlayerdown">
					<div>
						<p>{{comment.body}}</p> 
						<v-btn text>点赞</v-btn>
						<v-btn text>踩他</v-btn>
						<v-btn text @click="toreply(comment)">回复</v-btn>
						<v-btn text>举报</v-btn>
						<v-btn text @click="todelete(comment)" v-if="loginId === comment.author">删除</v-btn>
					</div>
					<BiuBox v-show="showReplyId === comment.id" :CommentLayer="CommentLayer"></BiuBox>
				</div>
			</v-col>
			<SubBiuList :comment="comment.replies" v-if="comment.author_avatar"></SubBiuList>
		</v-row>
		<v-row><v-btn @click="getprevious">上一页</v-btn><v-spacer></v-spacer><v-btn @click="getnext">下一页</v-btn></v-row>
	</div>
</template>

<script>
	import {getcomment,deletecomment} from '@/network/Comment/Comment.js'
	import BiuBox from '@/views/Comment/BiuBox.vue'
	import SubBiuList from '@/views/Comment/SubBiuList.vue'
	export default{
		name:"BiuList",
		data(){
			return{
				commentsobj:{
					replies:[]
				},
				nextcommentsurl:null,
				previouscommentsurl:null,
				showReplyId: '',
				loginId:null,
				CommentLayer:null,
				RootComment:{
					"id": 0,
					"content_type": 0,
					"object_id": 0,
					"body": "",
					"create_at": null,
					"author": 0,
					"comment_author": "fake",
					"author_avatar": "https://randomuser.me/api/portraits/men/81.jpg",
					"root": null,
					"parent": null,
					"reply_to": null,
					"get_content_type": null,
					"replies": null
				}
			}
		},
		components:{
			BiuBox,
			SubBiuList
		},
		props:{
			ContentType:{
				type:Number,
				default:null
			},
			ObjectId:{
				type:Number,
				default:null
			},
			CommentUrl:{
				type:String,
				default:"http://127.0.0.1:8000/api/c/comments/"
			}
		},
		mounted() {
			this.getcommentlist(this.ContentType,this.ObjectId,this.CommentUrl)
			if(localStorage.getItem('userid')){
				this.loginId = parseInt(localStorage.getItem('userid'))
			}
		},
		inject: ['reload'], 
		methods:{
			getcommentlist(ContentType,ObjectId,CommentUrl){
				let that = this
				getcomment(ContentType,ObjectId,CommentUrl).then(res=>{
					that.RootComment['replies'] = res.data.results
					that.commentsobj = this.RootComment
					that.nextcommentsurl = res.data.next
					that.previouscommentsurl = res.data.previous
				}).catch(err=>{
					console.log(err)
				})
			},
			toreply(commentlayer){
				if(!this.showReplyId){
					this.showReplyId = commentlayer.id
					this.CommentLayer = commentlayer
				}
				else{
					this.showReplyId = ''
					this.CommentLayer = null
				}
			},
			todelete(commentlayer){
				deletecomment(this.CommentUrl,commentlayer).then(res=>{
					this.reload() //局部刷新
				}).catch(err=>{
					console.log(err)
				})
			},
			getnext(){
				if(this.nextcommentsurl){
					this.getcommentlist(this.ContentType,this.ObjectId,this.nextcommentsurl)
				}
			},
			getprevious(){
				if(this.previouscommentsurl){
					this.getcommentlist(this.ContentType,this.ObjectId,this.previouscommentsurl)
				}
			}
		}
	}
</script>

<style scoped="scoped">
	.commentlist{
		display: flex;
		flex-direction: column;
	}
	.commentlayer .replylayer{
		display: flex;
		flex-direction: row;
	}

</style>
