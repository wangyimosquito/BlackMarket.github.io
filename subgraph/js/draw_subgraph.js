function draw_subgraph(json_name, force_strength){
    let theme_obj = theme_purple()
    document.getElementById("force-container").innerHTML = ""
    var dom = document.getElementById('force-container');
    dom.removeAttribute('_echarts_instance_')
    echarts.registerTheme('theme_purple', theme_obj)
    var myChart = echarts.init(dom, 'theme_purple', {
      // renderer: 'canvas',
      // useDirtyRect: false
    });
    myChart.clear(this.option);
    var app = {};
    var option;

    // myChart.showLoading();
    // myChart.showLoading();
    $.get(json_name, function (webkitDep) {
      myChart.hideLoading();
      option = {
        tooltip: {
          trigger: 'item',
          position: 'right',
          textStyle: {
            fontSize: 10
          }
        },
        legend: {
          data: ['Domain', 'IP', 'Cert', 'Whois_Info', 'IP_Info'],
          right: '17%',
          top: '8'
        },
        // title : {
        //   text: "Property Subgraph",
        //   padding: [10, 0, 0, 80],
        //   top : '3.5'
        // },
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
              // friction: 1
            },
            edges: webkitDep.links,
            // roam: true,
            // itemStyle: {
            //   shadowBlur: 1
            // }
          }
        ]
      };
      myChart.setOption(option);
    });

    if (option && typeof option === 'object') {
      myChart.setOption(option);
    }

    window.addEventListener('resize', myChart.resize);
}

function draw_core(json_name, force_strength){
  let theme_obj = theme_purple_invert()
  document.getElementById("force-container").innerHTML = ""
  var dom = document.getElementById('force-container')
  dom.removeAttribute('_echarts_instance_')
  echarts.registerTheme('theme_purple_invert', theme_obj)
  var myChart = echarts.init(dom, 'theme_purple_invert', {
    // renderer: 'canvas',
    // useDirtyRect: false
  });
  myChart.clear(this.option);
  var app = {};
  var option;

  // myChart.showLoading();
  // myChart.showLoading();
  $.get(json_name, function (webkitDep) {
    myChart.hideLoading();
    option = {
      tooltip: {
        trigger: 'item',
        position: 'right',
        textStyle: {
          fontSize: 10
        }
      },
      legend: {
        data: ['Core Property', 'Other Property'],
        right: '20%',
        top: '8'
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
              layoutAnimation : true
          },
          edges: webkitDep.links,
          // roam: true
        }
      ]
    };
    myChart.setOption(option);
  });

  if (option && typeof option === 'object') {
    myChart.setOption(option);
  }

  window.addEventListener('resize', myChart.resize);
}

function draw_dirty(json_name, force_strength){
  let theme_obj = theme_multi_purple()
  document.getElementById("force-container").innerHTML = ""
  var dom = document.getElementById('force-container')
  dom.removeAttribute('_echarts_instance_')
  echarts.registerTheme('theme_multi_purple', theme_obj)
  var myChart = echarts.init(dom, 'theme_multi_purple', {
    // renderer: 'canvas',
    // useDirtyRect: false
  });
  myChart.clear(this.option);
  var app = {};
  var option;

  $.get(json_name, function (webkitDep) {
    myChart.hideLoading();
    option = {
      tooltip: {
        trigger: 'item',
        position: 'right',
        textStyle: {
          fontSize: 10
        }
      },
      legend: [{
        top: '8',
        // padding: [10, 65, 20, 20],
        // orient: 'vertical',
        right: '15%',
        data: ['Clean', 'Erotic', 'Gambling', 'Illegal Trade', 'Gun']
      },
      {
        top: '35',
        // padding: [10, 65, 20, 20],
        // orient: 'vertical',
        right: '15%',
        data: ['Scam', 'Hacker', 'Illegal Payment', 'Drug']
      },
      {
        top: '62',
        // padding: [10, 65, 20, 20],
        // orient: 'vertical',
        right: '15%',
        data: ['Other indstry', 'Mixed Industry']
      }
      ],

      // legend: {
      //   data: ['Erotic', 'Gambling', 'Illegal Trade', 'Gun', 'Scam', 'Hacker', 'Illegal Payment', 'Drug',  'Other indstry', 'Mixed Industry', 'Clean'],
      //   right: '0%',
      //   top: '8'
      // },
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
              layoutAnimation : true
          },
          edges: webkitDep.links,
          // roam: true
        }
      ]
    };
    myChart.setOption(option);
  });

  if (option && typeof option === 'object') {
    myChart.setOption(option);
  }

  window.addEventListener('resize', myChart.resize);
}