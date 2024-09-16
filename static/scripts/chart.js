
    am4core.ready(function () {

      // Themes begin
      am4core.useTheme(am4themes_dark);
      am4core.useTheme(am4themes_animated);
      // Themes end

      var chart = am4core.create("chartdiv", am4plugins_timeline.SerpentineChart);
      chart.curveContainer.padding(50, 20, 50, 20);
      chart.levelCount = 4;
      chart.yAxisRadius = am4core.percent(25);
      chart.yAxisInnerRadius = am4core.percent(-25);
      chart.maskBullets = false;

      var colorSet = new am4core.ColorSet();
      colorSet.saturation = 0.5;

      var today = new Date();
      var dd = String(today.getDate()).padStart(2, '0');
      var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
      var yyyy = today.getFullYear();

      today = yyyy + '/' + mm + '/' + dd;
      chart.data = [
        {
          "category": "Job",
          "start": "2018-07-01",
          "end": "2020-09-19",
          "color": colorSet.getIndex(10),
          "task": "Daltile: Predictive Maintenance Engineer"
        }, {
          "category": "Job",
          "start": "2016-9-01",
          "end": "2017-09-01",
          "color": colorSet.getIndex(10),
          "task": "Yazaki Intern: Electrical Designe"
        }, {
          "category": "Job",
          "start": "2020-12-14",
          "end": "2021-12-14",
          "color": colorSet.getIndex(10),
          "task": "Acuity Brands Lighting: Test Technician"
        }, {
          "category": "Job",
          "start": "2022-01-10",
          "end": "2022-08-10",
          "color": colorSet.getIndex(10),
          "task": "Yazaki: Validation Engineer"
        }, {
          "category": "Job",
          "start": "2023-04-17",
          "end": today,
          "color": colorSet.getIndex(10),
          "task": "ENG Soluciones: Odoo Developer"
        }, 
        {
          "category": "Courses",
          "start": "2015-06-01",
          "end": "2015-12-01",
          "color": colorSet.getIndex(15),
          "task": "LabVIEW CLAD Certification"
        },
        {
          "category": "Courses",
          "start": "2023-04-17",
          "end": "2024-02-01",
          "color": colorSet.getIndex(15),
          "task": "Oddo Technical Training"
        }, {
          "category": "Courses",
          "start": "2020-07-01",
          "end": "2022-08-10",
          "color": colorSet.getIndex(15),
          "task": "Platzi: Programming Softwares"
        }, {
          "category": "Courses",
          "start": "2016-09-15",
          "end": "2018-12-01",
          "color": colorSet.getIndex(15),
          "task": "English: Quick Learning"
        }, {
          "category": "Courses",
          "start": "2019-05-01",
          "end": "2020-04-01",
          "color": colorSet.getIndex(15),
          "task": "Deutch: CCA"
        }, {
          "category": "Education",
          "start": "2010-06-01",
          "end": "2016-01-01",
          "color": colorSet.getIndex(0),
          "task": "University: Electrical and Automation Engineer"
        }, {
          "category": "Education",
          "start": "2017-03-01",
          "end": "2017-12-01",
          "color": colorSet.getIndex(0),
          "task": "University: Thesis"
        }, {
          "category": "Power Electronics Lab",
          "start": "2015-06-01",
          "end": "2017-02-01",
          "color": colorSet.getIndex(7),
          "task": "Inter"
        }];

      chart.dateFormatter.dateFormat = "yyyy-MM-dd";
      chart.dateFormatter.inputDateFormat = "yyyy-MM-dd";
      chart.fontSize = 11;


      var categoryAxis = chart.yAxes.push(new am4charts.CategoryAxis());
      categoryAxis.dataFields.category = "category";
      categoryAxis.renderer.grid.template.disabled = true;
      categoryAxis.renderer.labels.template.paddingRight = 10;
      categoryAxis.renderer.minGridDistance = 10;
      categoryAxis.renderer.innerRadius = -60;
      categoryAxis.renderer.radius = 60;


      var dateAxis = chart.xAxes.push(new am4charts.DateAxis());
      dateAxis.renderer.minGridDistance = 70;
      dateAxis.baseInterval = { count: 1, timeUnit: "day" };
      dateAxis.renderer.tooltipLocation = 0;
      dateAxis.startLocation = -0.5;
      dateAxis.renderer.line.strokeDasharray = "1,4";
      dateAxis.renderer.line.strokeOpacity = 0.6;
      dateAxis.tooltip.background.fillOpacity = 0.2;
      dateAxis.tooltip.background.cornerRadius = 5;
      dateAxis.tooltip.label.fill = new am4core.InterfaceColorSet().getFor("alternativeBackground");
      dateAxis.tooltip.label.paddingTop = 7;

      var labelTemplate = dateAxis.renderer.labels.template;
      labelTemplate.verticalCenter = "middle";
      labelTemplate.fillOpacity = 0.7;
      labelTemplate.background.fill = new am4core.InterfaceColorSet().getFor("background");
      labelTemplate.background.fillOpacity = 1;
      labelTemplate.padding(7, 7, 7, 7);

      var series = chart.series.push(new am4plugins_timeline.CurveColumnSeries());
      series.columns.template.height = am4core.percent(20);
      series.columns.template.tooltipText = "{category}: {task}: [bold]{openDateX}[/] - [bold]{dateX}[/]  ";

      series.dataFields.openDateX = "start";
      series.dataFields.dateX = "end";
      series.dataFields.categoryY = "category";
      series.columns.template.propertyFields.fill = "color"; // get color from data
      series.columns.template.propertyFields.stroke = "color";
      series.columns.template.strokeOpacity = 0;

      var bullet = series.bullets.push(new am4charts.CircleBullet());
      bullet.circle.radius = 5;
      bullet.circle.strokeOpacity = 0;
      bullet.propertyFields.fill = "color";
      bullet.locationX = 0;


      var bullet2 = series.bullets.push(new am4charts.CircleBullet());
      bullet2.circle.radius = 5;
      bullet2.circle.strokeOpacity = 0;
      bullet2.propertyFields.fill = "color";
      bullet2.locationX = 1;


      var imageBullet1 = series.bullets.push(new am4plugins_bullets.PinBullet());
      imageBullet1.disabled = true;
      imageBullet1.propertyFields.disabled = "disabled1";
      imageBullet1.locationX = 1;
      imageBullet1.circle.radius = 20;
      imageBullet1.propertyFields.stroke = "color";
      imageBullet1.background.propertyFields.fill = "color";
      imageBullet1.image = new am4core.Image();
      imageBullet1.image.propertyFields.href = "image1";

      var imageBullet2 = series.bullets.push(new am4plugins_bullets.PinBullet());
      imageBullet2.disabled = true;
      imageBullet2.propertyFields.disabled = "disabled2";
      imageBullet2.locationX = 0;
      imageBullet2.circle.radius = 20;
      imageBullet2.propertyFields.stroke = "color";
      imageBullet2.background.propertyFields.fill = "color";
      imageBullet2.image = new am4core.Image();
      imageBullet2.image.propertyFields.href = "image2";


      var eventSeries = chart.series.push(new am4plugins_timeline.CurveLineSeries());
      eventSeries.dataFields.dateX = "eventDate";
      eventSeries.dataFields.categoryY = "category";
      eventSeries.data = [
        { category: "Education", eventDate: "2015-06-01", letter: "LabVIEW", description: "Starting Developing whit LabVIEW" },
        { category: "Job", eventDate: "2020-10-01", letter: "Python", description: "Starting Developing whit Python" },
        { category: "Education", eventDate: "2014-02-10", letter: "Assembly", description: "Starting Developing whit Assembly" },
        { category: "Job", eventDate: "2021-03-01", letter: "Shell Windows", description: "Starting Developing whit shell windows" },
        { category: "Education", eventDate: "2021-04-01", letter: "Shell Linux", description: "Starting Developing whit shell linux" },
        { category: "Job", eventDate: "2020-12-14", letter: "Git", description: "Starting to work whit Git" }

      ];
      eventSeries.strokeOpacity = 0;

      var flagBullet = eventSeries.bullets.push(new am4plugins_bullets.FlagBullet())
      flagBullet.label.propertyFields.text = "letter";
      flagBullet.locationX = 0;
      flagBullet.tooltipText = "{description}";

      chart.scrollbarX = new am4core.Scrollbar();
      chart.scrollbarX.align = "center"
      chart.scrollbarX.width = am4core.percent(85);

      var cursor = new am4plugins_timeline.CurveCursor();
      chart.cursor = cursor;
      cursor.xAxis = dateAxis;
      cursor.yAxis = categoryAxis;
      cursor.lineY.disabled = true;
      cursor.lineX.strokeDasharray = "1,4";
      cursor.lineX.strokeOpacity = 1;

      dateAxis.renderer.tooltipLocation2 = 0;
      categoryAxis.cursorTooltipEnabled = false;


    }); // end am4core.ready()

