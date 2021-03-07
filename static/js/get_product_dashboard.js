var worksheet = new Vue({
    el: '#get_product_dashboard',
    data: {
        isFetching:true,
        get_product_sheets:[],
        dict:{},
        squad_select:0,
        date_select:null,
        warehouse_select:0,
        warehouses:null,
        page:1,
        paginate_select:20,
        serial_number_input:null,
        show_id:null,
        has_next_page:true,
        productss:null,
    },
    created(){
        this.isFetching=true
        axios.get('/search_get_product_sheet/',{params:{serial_number:this.serial_number_input,squad:this.squad_select,warehouse:this.warehouse_select,page:this.page,size:this.paginate_select}})
        .then(res => {
            console.log(res.data)
            this.get_product_sheets=res.data.data
            this.dict=res.data.dict_data
            this.isFetching=false
        }).catch(err => { console.error(err);   })

        
    },
    methods:{
        update_warehouse(){
            this.warehouse_select=0
            axios.get('/get_squad_warehouses/'+this.squad_select)
            .then(res => {
                this.warehouses=res.data
                this.update_data()
            })
        },
        update_data(){
            this.isFetching=true
            this.page=1
            axios.get('/search_get_product_sheet/',{params:{serial_number:this.serial_number_input,squad:this.squad_select,warehouse:this.warehouse_select,date:this.date_select,page:this.page,size:this.paginate_select}})
            .then(res => {
                console.log(res.data)
                this.get_product_sheets=res.data.data
                this.dict=res.data.dict_data
                this.isFetching=false
            }).catch(err => { console.error(err);   })
        },
        next_page(){
            if(window.scrollY>=document.body.scrollHeight-document.body.offsetHeight && this.has_next_page){
                this.has_next_page=false
                this.page+=1
                axios.get('/search_get_product_sheet/',{params:{serial_number:this.serial_number_input,squad:this.squad_select,warehouse:this.warehouse_select,date:this.date_select,page:this.page,size:this.paginate_select}})
                .then(res => {
                    this.get_product_sheets=this.get_product_sheets.concat(res.data.data)
                    this.dict=res.data.dict_data
                }).catch(err => { this.has_next_page=false   })
            }
        },
        modify(id){
            window.open('/update_worksheet_page/'+id)
        },
        del(id){
            result=window.confirm('確定刪除?')
            if( result ){
                axios.delete('/get_product_sheet_detail/'+id)
                .then(res => {
                    window.alert('刪除成功')
                    location.reload()
                }) .catch(err => { console.error(err);  })
            }
        },
        show_detail(id){
            axios.get('/get_get_product_sheet_productss/'+id)
            .then(res => {
                this.productss=res.data
                console.log(res.data)
                if(this.show_id==id){
                    this.show_id=null
                    return
                }   
                this.show_id=id
                console.log('ok')
            }).catch(err => { console.error(err);   })
        },
    }
})