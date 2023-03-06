function draw_link(json_name, force_strength){
    let theme_obj = theme_purple()
    document.getElementById("link-container").innerHTML = ""
    var dom = document.getElementById('link-container');
    dom.removeAttribute('_echarts_instance_')
    echarts.registerTheme('theme_purple', theme_obj)
    var myChart = echarts.init(dom, 'theme_purple', {
      // renderer: 'canvas',
      // useDirtyRect: false
    });
    var app = {};
    var option;

    // myChart.showLoading();
    // myChart.showLoading();
    $.get(json_name, function (webkitDep) {
      myChart.hideLoading();
      option = {
        tooltip: {
          trigger: 'item',
          position: 'left',
          transitionDuration: 0,
          textStyle: {
            fontSize: 10
          }
        },
        legend: {
          data: ['Domain', 'IP', 'Cert', 'Whois_Info', 'IP_Info'],
          left: '55',
          orient: 'vertical',
          padding: [25, 65, 20, 0],
          itemGap: 17,
          top: '50'
        },
        title : {
          text: "Critical Links",
          padding: [20, 0, 0, 50],
          top : '3.5'
        },
        series: [
          {
            type: 'graph',
            layout: 'force',
            // legendHoverLink : true, //是否启用图例 hover(悬停) 时的联动高亮。
            // hoverAnimation : true, //是否开启鼠标悬停节点的显示动画
            // animation: false,
            label: {
              show: false,
              // position: 'right',
              // formatter: '{b}',
              // offset: [20, 20],
              emphasis : {//高亮状态
                show: false
              }
            },
            draggable: true,
            data: webkitDep.nodes.map(function (node, idx) {
              node.id = idx;
              return node;
            }),
            focusNodeAdjacency: true,
            categories: webkitDep.categories,
            force: {
              edgeLength: force_strength[0],
              repulsion: force_strength[1],
              gravity: force_strength[2],
              layoutAnimation : true,
              initLayout: 'circular'
              // friction: 1
            },
            edges: webkitDep.links,
            // roam: 'move',
            // itemStyle: {
            //   shadowBlur: 1
            // }
          }
        ]
      };
    //   myChart.on('mouseup',function(params){
    //     var option=myChart.getOption();
    //     option.series[0].data[params.dataIndex].x=params.event.offsetX;
    //     option.series[0].data[params.dataIndex].y=params.event.offsetY;
    //     option.series[0].data[params.dataIndex].fixed=true;
    //     myChart.setOption(option);
    //     });
      myChart.setOption(option);
    });

    if (option && typeof option === 'object') {
      myChart.setOption(option);
    }

    window.addEventListener('resize', myChart.resize);
}

function draw_core_link(json_name, force_strength){
  let theme_obj = theme_purple_invert()
  document.getElementById("link-container").innerHTML = ""
  var dom = document.getElementById('link-container');
  dom.removeAttribute('_echarts_instance_')
  echarts.registerTheme('theme_purple_invert', theme_obj)
  var myChart = echarts.init(dom, 'theme_purple_invert', {
    // renderer: 'canvas',
    // useDirtyRect: false
  });
  var app = {};
  var option;

  // myChart.showLoading();
  // myChart.showLoading();
  $.get(json_name, function (webkitDep) {
    myChart.hideLoading();
    option = {
      tooltip: {
        trigger: 'item',
        position: 'left',
        transitionDuration: 0,
        textStyle: {
          fontSize: 10
        }
      },
      legend: {
        data: ['Core Property', 'Other Property'],
        left: '55',
        orient: 'vertical',
        padding: [40, 65, 20, 0],
        // selectedMode: false,
        itemGap: 40,
        top: '50'
      },
      title : {
        text: "Critical Links",
        padding: [20, 0, 0, 50],
        top : '3.5'
      },
      series: [
        {
          type: 'graph',
          layout: 'force',
          // legendHoverLink : true, //是否启用图例 hover(悬停) 时的联动高亮。
          // hoverAnimation : true, //是否开启鼠标悬停节点的显示动画
          // animation: false,
          label: {
            show: false,
            // position: 'right',
            // formatter: '{b}',
            // offset: [20, 20],
            emphasis : {//高亮状态
              show: false
            }
          },
          draggable: true,
          data: webkitDep.nodes.map(function (node, idx) {
            node.id = idx;
            return node;
          }),
          focusNodeAdjacency: true,
          categories: webkitDep.categories,
          force: {
            edgeLength: force_strength[0],
            repulsion: force_strength[1],
            gravity: force_strength[2],
            layoutAnimation : true,
            initLayout: 'circular'
            // friction: 1
          },
          edges: webkitDep.links,
          // roam: 'move',
          // itemStyle: {
          //   shadowBlur: 1
          // }
        }
      ]
    };
  //   myChart.on('mouseup',function(params){
  //     var option=myChart.getOption();
  //     option.series[0].data[params.dataIndex].x=params.event.offsetX;
  //     option.series[0].data[params.dataIndex].y=params.event.offsetY;
  //     option.series[0].data[params.dataIndex].fixed=true;
  //     myChart.setOption(option);
  //     });
    myChart.setOption(option);
  });

  if (option && typeof option === 'object') {
    myChart.setOption(option);
  }

  window.addEventListener('resize', myChart.resize);
}
