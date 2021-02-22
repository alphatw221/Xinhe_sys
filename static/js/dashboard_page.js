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
    },
    created(){
        this.isFetching=true
        axios.get('/worksheet_list/')
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
        modify(id){
            window.open('/update_worksheet_page/'+id)
        },
        delete(id){
            result=window.confirm('確定刪除?')
            if( result ){
                axios.delete('worksheet_detail/'+id)
                .then(res => {
                    window.alert('刪除成功')
                    location.reload()
                }) .catch(err => { console.error(err);  })
            }
        }
    }
})