var worksheet = new Vue({
    el: '#update_get_product_sheet',
    data: {
      get_product_sheet:null,
      isFetching:true,
      products:[],
      warehouses:[],
      out_warehouses:[],
      export_check:false,
    },
    created(){
        this.isFetching=true
        const url = window.location.href
        const parts=url.split('/')
        axios.get('/get_product_sheet_detail/'+parts[parts.length-1])
        .then(res => {
            console.log(res.data)
            this.get_product_sheet=res.data.get_product_sheet
            this.products=res.data.products
            this.isFetching=false
        }).catch(err => { console.error(err); })
    },
    methods:{
        add_products(){
            this.products.push({product:null,code:null,name:"--",unit:'--',warehouse:this.get_product_sheet.warehouse,date:this.get_product_sheet.date,use_product_sheet:this.get_product_sheet.id})
        },
        submit(){
            data=[]
            for(i=0;i<this.products.length;i++){
                data.push({product:this.products[i].product,
                    amount:this.products[i].amount,
                    warehouse:this.get_product_sheet.warehouse,
                    date:this.get_product_sheet.date,
                    get_product_sheet:this.get_product_sheet.id,
                    out_warehouse:this.get_product_sheet.out_warehouse,
                    })
            }
            axios.put('/get_product_sheet_detail/'+this.get_product_sheet.id,{get_product_sheet:this.get_product_sheet,get_product_sheet_productss:data})
            .then(res => {
                this.export_data=res.data['data']
                if(this.export_check){
                  this.export()
                }
                window.alert(res.data['message'])
                location.reload()
            })
            .catch(err => {
                window.alert('更新資料錯誤')
            })
            
        },
        search_product(index){
            axios.get('/get_product_with_code/',{params:{code:this.products[index].code}})
                .then(res => {
                    this.products[index].name=res.data.name
                    this.products[index].unit=res.data.unit
                    this.products[index].product=res.data.id
                })
        },
        cancel_product(index){
            this.products.splice(index,1)
        },
        update_warehouse(){
            this.get_product_sheet.warehouse=null
            axios.get('/get_squad_warehouses/'+this.get_product_sheet.squad)
            .then(res => {
                this.get_product_sheet.warehouses=res.data
            })
            
        },
        update_out_warehouse(){
          this.get_product_sheet.out_warehouse=null
          axios.get('/get_squad_warehouses/'+this.get_product_sheet.out_squad)
          .then(res => {
              this.get_product_sheet.out_warehouses=res.data
          })
          
      },
      export(){
        var sheet=this.export_data.get_product_sheet
        var productss=this.export_data.get_product_sheet_productss

        file_name='領貨單'+sheet.serial_number+'.xlsx'
        var excel = '<table id="expoetTable">'
        excel += '<tr><th>領料單</th></tr>'
        excel += '<tr><td>單號</td><td>'+sheet.serial_number+'</td></tr>'
        excel += '<tr><td>工班</td><td>'+sheet.squad+'</td></tr>'
        excel += '<tr><td>倉庫</td><td>'+sheet.warehouse+'</td></tr>'
        excel += '<tr><td>發料公司</td><td>'+sheet.out_squad+'</td></tr>'
        excel += '<tr><td>發料倉庫</td><td>'+sheet.out_warehouse+'</td></tr>'
        excel += '<tr><td>日期</td><td>'+sheet.date+'</td></tr>'
        excel += '<tr><th>料號</th><th>料名</th> <th></th><th></th> <th>數量</th><th>單位</th></tr>'
        for (i=0;i<10;i++){
          if(productss[i]){
            excel += '<tr><td>'+productss[i].code+'</td>'
            excel += '<td>'+productss[i].name+'</td><td></td><td></td>'
            excel += '<td>'+productss[i].amount+'</td>'
            excel += '<td>'+productss[i].unit+'</td></tr>'
          }else{
            excel+='<tr></tr>'
          }
          
        }
        excel += '<tr></tr>'
        excel += '<tr></tr>'
        excel += '<tr><td>發料人簽名:</td><td>___________________</td></tr>'
        excel += '<tr></tr>'
        excel += '<tr></tr>'
        excel += '<tr><td>領料人簽名:</td><td>___________________</td></tr>'
        excel += '<tr><th>______________________________________________________________________</th></tr>'
        excel +='<tr></tr>'
        excel += '<tr><th>領料單</th></tr>'
        excel += '<tr><td>單號</td><td>'+sheet.serial_number+'</td></tr>'
        excel += '<tr><td>工班</td><td>'+sheet.squad+'</td></tr>'
        excel += '<tr><td>倉庫</td><td>'+sheet.warehouse+'</td></tr>'
        excel += '<tr><td>發料公司</td><td>'+sheet.out_squad+'</td></tr>'
        excel += '<tr><td>發料倉庫</td><td>'+sheet.out_warehouse+'</td></tr>'
        excel += '<tr><td>日期</td><td>'+sheet.date+'</td></tr>'
        excel += '<tr><th>料號</th><th>料名</th> <th></th><th></th> <th>數量</th><th>單位</th></tr>'
        for (i=0;i<10;i++){
          if(productss[i]){
            excel += '<tr><td>'+productss[i].code+'</td>'
            excel += '<td>'+productss[i].name+'</td><td></td><td></td>'
            excel += '<td>'+productss[i].amount+'</td>'
            excel += '<td>'+productss[i].unit+'</td></tr>'
            
          }else{
            excel+='<tr></tr>'
          }
        }
        excel += '<tr></tr>'
        excel += '<tr></tr>'
        excel += '<tr><td>發料人簽名:</td><td>___________________</td></tr>'
        excel += '<tr></tr>'
        excel += '<tr></tr>'
        excel += '<tr><td>領料人簽名:</td><td>___________________</td></tr>'
        excel+='</table>'
        var objE = document.createElement('div') // 因爲我們這裏的數據是string格式的,但是js-xlsx需要dom格式,則先新建一個div然後把數據加入到innerHTML中,在傳childNodes[0]即使dom格式的數據
        objE.innerHTML = excel
        var sheet = XLSX.utils.table_to_sheet(objE.childNodes[0], { raw: true })// 將一個table對象轉換成一個sheet對象,raw爲true的作用是把數字當成string,身份證不轉換成科學計數法
        this.openDownloadDialog(this.sheet2blob(sheet, '領貨單'), file_name)
        this.export_data.get_product_sheet_productss.splice(0,10)
        if (this.export_data.get_product_sheet_productss.length>0){
          this.export()
        }
    },
    sheet2blob(sheet, sheetName) {
        sheetName = sheetName || 'sheet1' // 不存在sheetName時使用sheet1代替
        var workbook = {
          SheetNames: [sheetName],
          Sheets: {}
        }
        workbook.Sheets[sheetName] = sheet // 生成excel的配置項
      
        var wopts = {
          bookType: 'xlsx', // 要生成的文件類型
          bookSST: false, // 是否生成Shared String Table，官方解釋是，如果開啓生成速度會下降，但在低版本IOS設備上有更好的兼容性
          type: 'binary' // 二進制格式
        }
        var wbout = XLSX.write(workbook, wopts)
        var blob = new Blob([s2ab(wbout)], {
          type: 'application/octet-stream'
        }) // 字符串轉ArrayBuffer
        function s2ab(s) {
          var buf = new ArrayBuffer(s.length)
          var view = new Uint8Array(buf)
          for (var i = 0; i != s.length; ++i) view[i] = s.charCodeAt(i) & 0xFF
          return buf
        }
        return blob
      },
      openDownloadDialog(url, saveName) {
        if (typeof url === 'object' && url instanceof Blob) {
          url = URL.createObjectURL(url) // 創建blob地址
        }
        var aLink = document.createElement('a')
        aLink.href = url
        aLink.download = saveName || '' // HTML5新增的屬性，指定保存文件名，可以不要後綴，注意，file:///模式下不會生效
        var event
        if (window.MouseEvent) event = new MouseEvent('click')
        else {
          event = document.createEvent('MouseEvents')
          event.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null)
        }
        aLink.dispatchEvent(event)
      }
    }
})