var worksheet = new Vue({
    el: '#dashboard',
    data: {
        isFetching:false,
        worksheets:[],
        dict:{},
        n:1,
        squad_select:0,
        status_select:0,
        type1_select:0,
        type2_select:0,
        region_select:0,
        project_select:0,
        page:1,
        paginate_select:20,
        serial_number_input:null,
    },
    created(){
        this.isFetching=true
        axios.get('/worksheet_list/',{params:{page:this.page,size:this.paginate_select}})
        .then(res => {
            this.worksheets=res.data
            axios.get('/get_all_dict/')
            .then(res => {
                this.dict=res.data
                this.isFetching=false
            }).catch(err => { console.error(err);   })

        }).catch(err => { console.error(err);   })

        
    },
    methods:{
        update_data(){
            axios.get('/search_worksheet/',{params:{serial_number:this.serial_number_input,squad:this.squad_select,status:this.status_select,
                type1:this.type1_select,type2:this.type2_select,region:this.region_select,
                project:this.project_select,page:this.page,size:this.paginate_select}})
            .then(res => {
                this.worksheets=res.data

            }).catch(err => { console.error(err);   })
        },
        modify(id){
            window.open('/update_worksheet_page/'+id)
        },
        del(id){
            result=window.confirm('確定刪除?')
            if( result ){
                axios.delete('/worksheet_detail/'+id)
                .then(res => {
                    window.alert('刪除成功')
                    location.reload()
                }) .catch(err => { console.error(err);  })
            }
        }
    }
})