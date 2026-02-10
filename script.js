let lang = "en";
let chart;

function toggleLanguage() {
  lang = lang === "en" ? "ar" : "en";
  document.documentElement.dir = lang === "ar" ? "rtl" : "ltr";

  const text = {
    en: {
      title: "Economics Simulations",
      microTitle: "Microeconomics",
      microDesc: "Price Competition Simulation (Bertrand)",
      priceLabel: "Choose your price:",
      runBtn: "Run Simulation",
      macroTitle: "Macroeconomics",
      macroDesc: "Policy Simulations",
      coming: "Coming Soon",
      thPrice: "Price",
      thQuantity: "Quantity",
      thProfit: "Profit"
    },
    ar: {
      title: "محاكاة الاقتصاد",
      microTitle: "الاقتصاد الجزئي",
      microDesc: "محاكاة المنافسة السعرية",
      priceLabel: "اختر السعر:",
      runBtn: "تشغيل المحاكاة",
      macroTitle: "الاقتصاد الكلي",
      macroDesc: "محاكاة السياسات الاقتصادية",
      coming: "قريباً",
      thPrice: "السعر",
      thQuantity: "الكمية",
      thProfit: "الربح"
    }
  };

  for (let id in text[lang]) {
    document.getElementById(id).innerText = text[lang][id];
  }
}

function runSimulation() {
  const price = Number(document.getElementById("priceInput").value);
  const mc = Math.floor(Math.random() * 10) + 10;
  const demand = 120;
  const quantity = Math.max(0, demand - price);
  const profit = (price - mc) * quantity;

  document.getElementById("resPrice").innerText = price;
  document.getElementById("resQty").innerText = quantity;
  document.getElementById("resProfit").innerText = profit.toFixed(2);

  drawChart(price, quantity);
}

function drawChart(price, quantity) {
  const ctx = document.getElementById("chart").getContext("2d");

  if (chart) chart.destroy();

  chart = new Chart(ctx, {
    type: "line",
    data: {
      labels: ["0", "Price"],
      datasets: [{
        label: lang === "ar" ? "الطلب" : "Demand",
        data: [120, quantity],
        borderWidth: 2
      }]
    }
  });
}
