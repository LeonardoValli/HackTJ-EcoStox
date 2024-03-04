from flask import Flask, render_template, request, send_file, send_from_directory

app = Flask(__name__)

@app.route('/')
def ask_questions():
    return render_template('index.html')


@app.route('/generic')
def generic():
    return render_template('generic.html')

@app.route('/elements')
def elements():
    return render_template('elements.html')


@app.route('/page2')
def page2():
    return render_template('home.html')


@app.route('/page3')
def page3():
    return render_template('page3.html')

@app.route('/page4')
def page4():
    return render_template('page4.html')

@app.route('/page5')
def page5():
    return render_template('page5.html')

@app.route('/page6')
def page6():
    return render_template('page6.html')


@app.route('/recommendations')
def recs():
    return render_template('recs.html')

@app.route('/EnviroFriendlyStocks')
def stocks():
    return render_template('stocks.html')

@app.route('/stockReport', methods = ['GET', 'POST'])
def stock_report():
    return render_template('stockReport.html', stockRecs = choose_stocks(request.form.get("name"), request.form.get("type"), request.form.get("risk"), request.form.get("count")))


@app.route('/<folder>/<file>')
def file_finder(folder, file):
    return send_from_directory(folder, file)


@app.route('/<folder>/<folder2>/<file>')
def file_finder2(folder, folder2, file):
    directory = f"{folder}/{folder2}"
    return send_from_directory(directory, file)


def calculate_similarity(input_company, input_risk_rating, target_companies, environmental_data, risk_data):
    # Calculate cosine similarity between input company and target companies based on environmental impact and risk
    input_environmental_impact = environmental_data.get(input_company, 0)  # Assume 0 if environmental data not available

    similarities = {}
    # print(risk_data)
    # print(len(risk_data))
    # print(set(target_companies))
    # print(len(set(target_companies)))
    for company in target_companies:
        if risk_data[company] >= input_risk_rating:
            # print(company)
            target_environmental_impact = environmental_data.get(company, 0)  # Assume 0 if environmental data not available
            target_risk = risk_data.get(company, 3)  # Assume risk of 3 if data not available

            # Calculate cosine similarity based on environmental impact and risk
            # You may adjust the formula based on your preference or specific metrics
            similarity_score = target_environmental_impact * target_risk
            similarities[company] = similarity_score

    return similarities


def recommend_similar_company(input_company, input_sector, input_risk_rating, sector_list, environmental_data, risk_rating):

    # Calculate similarity based on environmental impact
    similarities = calculate_similarity(input_company, input_risk_rating, sector_list, environmental_data, risk_rating)
    print(similarities)
    # Recommend the company with the highest similarity
    recommended_company = max(similarities, key=similarities.get)

    return similarities, recommended_company

def choose_stocks(input_company, input_sector, input_risk_rating, num_wanted):

    # Stock tickers
    energy_companies = [
        "XOM",
        "CVX",
        "COP",
        "EOG",
        "OXY",
        "PSX",
        "MPC",
        "VLO",
        "HES",
        "DVN",
        "PXD",
        "APA",
        "NBL",
        "MRO",
        "NEE",
        "DUK",
        "SO",
        "D",
        "EXC",
        "AEP",
        "PCG",
        "XEL",
        "ED",
        "EIX"
    ]
    materials_companies = [
        "BHP",
        "RIO",
        "ECL",
        "DD",
        "FCX",
        "LIN",
        "NEM",
        "GOLD",
        "NTR",
        "VALE",
        "AAL",
        "SCCO",
        "MOS",
        "NCM",
        "WPM",
        "TECK",
        "AEM",
        "NUE",
        "MT",
        "PKX",
        "ALB",
        "PPG",
        "CF",
        "EMN",
        "APD",
        "FNV",
        "NTR",
        "RS",
        "GOLD",
        "FMG"
    ]
    industrial_companies = [
        "GE",
        "HON",
        "MMM",
        "CAT",
        "BA",
        "UTX",
        "UNP",
        "DE",
        "RTX",
        "LMT",
        "EMR",
        "ITW",
        "SIEGY",
        "UPS",
        "GD",
        "NOC",
        "WM",
        "AL",
        "CMI",
        "ABB",
        "EMR",
        "ROK",
        "SBGSY",
        "CSX",
        "HON",
        "ETN",
        "EMR",
        "PH",
        "PCP",
        "TXT"
    ]
    consumer_discretionary_companies = [
        "AMZN",
        "TSLA",
        "DIS",
        "NKE",
        "HD",
        "MCD",
        "SBUX",
        "BKNG",
        "LOW",
        "TGT",
        "CMCSA",
        "TJX",
        "NFLX",
        "LVMUY",
        "VWAGY",
        "YUM",
        "HD",
        "KO",
        "GM",
        "RACE",
        "PDD",
        "BKNG",
        "ADDYY",
        "PDD",
        "MAR",
        "RACE",
        "PDD",
        "HLT",
        "AAL",
        "CCL"
    ]
    consumer_staples_companies = [
        "PG",
        "KO",
        "PEP",
        "WMT",
        "CL",
        "NSRGY",
        "UL",
        "MDLZ",
        "COST",
        "MO",
        "KHC",
        "PM",
        "KMB",
        "DANOY",
        "DEO",
        "EL",
        "ADM",
        "BUD",
        "HSY",
        "STZ",
        "KDP",
        "MNST",
        "GIS",
        "K",
        "SYY",
        "TSN",
        "CPB",
        "MKC",
        "CLX",
        "CHD"
    ]
    healthcare_companies = [
        "JNJ",
        "PFE",
        "MRK",
        "UNH",
        "ABBV",
        "AMGN",
        "BMY",
        "LLY",
        "NVS",
        "GILD",
        "MDT",
        "ABT",
        "TMO",
        "VRTX",
        "AZN"
    ]
    financials_companies = [
        "JPM",
        "BAC",
        "WFC",
        "V",
        "MA",
        "BRK.B",
        "PYPL",
        "C",
        "GS",
        "MS",
        "AXP",
        "GS",
        "USB",
        "SCHW",
        "BLK",
        "SPGI",
        "SCHW",
        "COF",
        "BX",
        "CB",
        "MET",
        "AIG",
        "BK",
        "AFL",
        "MCO",
        "HIG",
        "TRV",
        "DFS",
        "PGR",
        "MMC"
    ]
    information_technology_companies = [
        "AAPL",
        "MSFT",
        "GOOGL",
        "FB",
        "INTC",
        "NVDA",
        "TSM",
        "ADBE",
        "CSCO",
        "CRM",
        "ORCL",
        "IBM",
        "ACN",
        "SAP",
        "PYPL",
        "TXN",
        "AVGO",
        "ASML",
        "ADBE",
        "NOW",
        "VMW",
        "AMAT",
        "QCOM",
        "MU",
        "HPQ",
        "DELL",
        "UBER",
        "TWTR",
        "SQ",
        "ZM"
    ]
    communication_services_companies = [
        "GOOGL",
        "FB",
        "TCEHY",
        "BABA",
        "NFLX",
        "T",
        "VZ",
        "CMCSA",
        "CHTR",
        "NTT",
        "SFTBY",
        "CHL",
        "TCEHY",
        "DTEGY",
        "TMUS",
        "TEF",
        "VOD",
        "CHU",
        "BCE",
        "DISH",
        "TLSYY",
        "ORAN",
        "AMX",
        "BT",
        "LBTYA",
        "RELIANCE",
        "AMX",
        "TU",
        "RCI",
        "LILA"
    ]
    utilities_companies = [
        "NEE",
        "DUK",
        "D",
        "SO",
        "AEP",
        "EXC",
        "PCG",
        "XEL",
        "ED",
        "EIX",
        "PCG",
        "SRE",
        "NGG",
        "EOAN",
        "ENGIY",
        "ENLAY",
        "CPYYY",
        "D",
        "PEG",
        "FE"
    ]
    real_estate_companies = [
        "AMT",
        "PLD",
        "SPG",
        "CCI",
        "EQIX",
        "AVB",
        "PSA",
        "DLR",
        "O",
        "WELL",
        "ESS",
        "ARE",
        "VTR",
        "BXP",
        "WY",
        "PEAK",
        "PEAK",
        "DRE",
        "EXR",
        "HST",
        "VICI",
        "SBAC",
        "WELL",
        "VNO",
        "FRT",
        "O",
        "MAA",
        "IRM",
        "INVH",
        "ARE"
    ]
    consumer_goods_companies = [
        "KO", "PEP", "NSRGY", "PG", "UL", "KHC", "MDLZ", "CL", "KMB", "GIS",
        "K", "CPB", "HSY", "CAG", "HRL", "CLX", "EL", "MKC", "TAP", "TSN",
        "SJM", "CHD", "NWL", "MAT", "HAS", "LEVI", "VFC", "NKE", "DIS", "MCD",
        "SBUX", "KO", "PEP", "MO", "PM", "BUD", "DEO", "BF.B", "STZ", "TAP",
        "KDP", "SAM", "HSY", "KHC", "CPB", "K", "GIS", "MDLZ", "SJM", "CAG",
        "MKC", "CLX", "KMB", "PG", "CL", "JNJ", "EL", "COTY", "REV", "EL"
    ]

    # Dictionary of sector to ticker mappings
    ticker_sector = {
        "energy": energy_companies,
        "materials": materials_companies,
        "industrial": industrial_companies,
        "consumer_discretionary": consumer_discretionary_companies,
        "consumer_staples": consumer_staples_companies,
        "healthcare": healthcare_companies,
        "financials": financials_companies,
        "information_technology": information_technology_companies,
        "communication_services": communication_services_companies,
        "utilities": utilities_companies,
        "real_estate": real_estate_companies,
        "consumer_goods": consumer_goods_companies
    }
    all_companies = sum(ticker_sector.values(), [])

    # Dictionary of ticker to environmental impact
    energy_to_environmental_impact = {
        "XOM": 0.31,
        "CVX": 0.36,
        "COP": 0.41,
        "EOG": 0.46,
        "OXY": 0.39,
        "PSX": 0.38,
        "MPC": 0.41,
        "VLO": 0.37,
        "HES": 0.44,
        "DVN": 0.52,
        "PXD": 0.49,
        "APA": 0.51,
        "NBL": 0.45,
        "MRO": 0.42,
        "NEE": 0.75,
        "DUK": 0.7,
        "SO": 0.72,
        "D": 0.73,
        "EXC": 0.68,
        "AEP": 0.71,
        "PCG": 0.4,
        "XEL": 0.72,
        "ED": 0.73,
        "EIX": 0.74
    }
    materials_to_environmental_impact = {
        "BHP": 0.55,
        "RIO": 0.58,
        "ECL": 0.65,
        "DD": 0.67,
        "FCX": 0.6,
        "LIN": 0.72,
        "NEM": 0.5,
        "GOLD": 0.51,
        "NTR": 0.68,
        "VALE": 0.54,
        "AAL": 0.35,
        "SCCO": 0.62,
        "MOS": 0.56,
        "NCM": 0.53,
        "WPM": 0.52,
        "TECK": 0.58,
        "AEM": 0.54,
        "NUE": 0.63,
        "MT": 0.6,
        "PKX": 0.58,
        "ALB": 0.68,
        "PPG": 0.7,
        "CF": 0.65,
        "EMN": 0.66,
        "APD": 0.75,
        "FNV": 0.52,
        "RS": 0.61,
        "FMG": 0.49
    }
    industrial_to_environmental_impact = {
        "GE": 0.67,
        "HON": 0.7,
        "MMM": 0.72,
        "CAT": 0.65,
        "BA": 0.68,
        "UTX": 0.71,
        "UNP": 0.74,
        "DE": 0.66,
        "RTX": 0.69,
        "LMT": 0.75,
        "EMR": 0.7,
        "ITW": 0.73,
        "SIEGY": 0.68,
        "UPS": 0.72,
        "GD": 0.71,
        "NOC": 0.73,
        "WM": 0.76,
        "AL": 0.69,
        "CMI": 0.67,
        "ABB": 0.67,
        "ROK": 0.68,
        "SBGSY": 0.68,
        "CSX": 0.72,
        "ETN": 0.69,
        "PH": 0.74,
        "PCP": 0.71,
        "TXT": 0.68
    }
    consumer_discretionary_to_environmental_impact = {
        "AMZN": 0.65,
        "TSLA": 0.8,
        "DIS": 0.7,
        "NKE": 0.75,
        "HD": 0.72,
        "MCD": 0.68,
        "SBUX": 0.73,
        "BKNG": 0.75,
        "LOW": 0.71,
        "TGT": 0.72,
        "CMCSA": 0.7,
        "TJX": 0.68,
        "NFLX": 0.7,
        "LVMUY": 0.74,
        "VWAGY": 0.76,
        "YUM": 0.7,
        "KO": 0.75,
        "GM": 0.7,
        "RACE": 0.75,
        "PDD": 0.7,
        "ADDYY": 0.74,
        "MAR": 0.72,
        "HLT": 0.73,
        "AAL": 0.35,
        "CCL": 0.4
    }
    consumer_staples_to_environmental_impact = {
        "PG": 0.76,
        "KO": 0.75,
        "PEP": 0.74,
        "WMT": 0.71,
        "CL": 0.72,
        "NSRGY": 0.77,
        "UL": 0.73,
        "MDLZ": 0.71,
        "COST": 0.72,
        "MO": 0.68,
        "KHC": 0.69,
        "PM": 0.71,
        "KMB": 0.71,
        "DANOY": 0.76,
        "DEO": 0.75,
        "EL": 0.73,
        "ADM": 0.68,
        "BUD": 0.75,
        "HSY": 0.71,
        "STZ": 0.72,
        "KDP": 0.71,
        "MNST": 0.7,
        "GIS": 0.71,
        "K": 0.72,
        "SYY": 0.71,
        "TSN": 0.7,
        "CPB": 0.71,
        "MKC": 0.73,
        "CLX": 0.72,
        "CHD": 0.71
    }
    healthcare_to_environmental_impact = {
        "JNJ": 0.78,
        "PFE": 0.77,
        "MRK": 0.76,
        "UNH": 0.75,
        "ABBV": 0.76,
        "AMGN": 0.75,
        "BMY": 0.76,
        "LLY": 0.76,
        "NVS": 0.77,
        "GILD": 0.75,
        "MDT": 0.76,
        "ABT": 0.77,
        "TMO": 0.77,
        "VRTX": 0.76,
        "AZN": 0.75
    }
    financials_to_environmental_impact = {
        "JPM": 0.7,
        "BAC": 0.69,
        "WFC": 0.68,
        "V": 0.75,
        "MA": 0.74,
        "BRK.B": 0.76,
        "PYPL": 0.72,
        "C": 0.71,
        "GS": 0.73,
        "MS": 0.72,
        "AXP": 0.74,
        "USB": 0.7,
        "SCHW": 0.71,
        "BLK": 0.75,
        "SPGI": 0.73,
        "COF": 0.7,
        "BX": 0.72,
        "CB": 0.73,
        "MET": 0.71,
        "AIG": 0.69,
        "BK": 0.7,
        "AFL": 0.71,
        "MCO": 0.74,
        "HIG": 0.7,
        "TRV": 0.73,
        "DFS": 0.7,
        "PGR": 0.71,
        "MMC": 0.72
    }
    information_technology_to_environmental_impact = {
        "AAPL": 0.78,
        "MSFT": 0.77,
        "GOOGL": 0.76,
        "FB": 0.75,
        "INTC": 0.74,
        "NVDA": 0.73,
        "TSM": 0.75,
        "ADBE": 0.76,
        "CSCO": 0.73,
        "CRM": 0.75,
        "ORCL": 0.73,
        "IBM": 0.71,
        "ACN": 0.74,
        "SAP": 0.73,
        "PYPL": 0.72,
        "TXN": 0.74,
        "AVGO": 0.75,
        "ASML": 0.76,
        "NOW": 0.75,
        "VMW": 0.73,
        "AMAT": 0.72,
        "QCOM": 0.72,
        "MU": 0.71,
        "HPQ": 0.72,
        "DELL": 0.72,
        "UBER": 0.71,
        "TWTR": 0.72,
        "SQ": 0.71,
        "ZM": 0.73
    }
    communication_services_to_environmental_impact = {
        "GOOGL": 0.76,
        "FB": 0.75,
        "TCEHY": 0.72,
        "BABA": 0.73,
        "NFLX": 0.74,
        "T": 0.71,
        "VZ": 0.72,
        "CMCSA": 0.72,
        "CHTR": 0.73,
        "NTT": 0.7,
        "SFTBY": 0.73,
        "CHL": 0.7,
        "DTEGY": 0.71,
        "TMUS": 0.72,
        "TEF": 0.71,
        "VOD": 0.72,
        "CHU": 0.7,
        "BCE": 0.71,
        "DISH": 0.71,
        "TLSYY": 0.7,
        "ORAN": 0.71,
        "AMX": 0.72,
        "BT": 0.71,
        "LBTYA": 0.73,
        "RELIANCE": 0.74,
        "TU": 0.71,
        "RCI": 0.72,
        "LILA": 0.72
    }
    utilities_to_environmental_impact = {
        "NEE": 0.75,
        "DUK": 0.7,
        "D": 0.73,
        "SO": 0.72,
        "AEP": 0.71,
        "EXC": 0.68,
        "PCG": 0.4,
        "XEL": 0.72,
        "ED": 0.73,
        "EIX": 0.74,
        "SRE": 0.74,
        "NGG": 0.75,
        "EOAN": 0.72,
        "ENGIY": 0.73,
        "ENLAY": 0.74,
        "CPYYY": 0.71,
        "PEG": 0.7,
        "FE": 0.71
    }
    real_estate_to_environmental_impact = {
        "AMT": 0.74,
        "PLD": 0.73,
        "SPG": 0.71,
        "CCI": 0.74,
        "EQIX": 0.75,
        "AVB": 0.72,
        "PSA": 0.71,
        "DLR": 0.73,
        "O": 0.72,
        "WELL": 0.72,
        "ESS": 0.73,
        "ARE": 0.72,
        "VTR": 0.71,
        "BXP": 0.72,
        "WY": 0.7,
        "PEAK": 0.71,
        "DRE": 0.71,
        "EXR": 0.73,
        "HST": 0.71,
        "VICI": 0.72,
        "SBAC": 0.74,
        "VNO": 0.72,
        "FRT": 0.71,
        "MAA": 0.72,
        "IRM": 0.71,
        "INVH": 0.72
    }
    consumer_goods_to_environmental_impact = {
        "KO": 0.75,
        "PEP": 0.74,
        "NSRGY": 0.77,
        "PG": 0.76,
        "UL": 0.73,
        "KHC": 0.71,
        "MDLZ": 0.72,
        "CL": 0.73,
        "KMB": 0.72,
        "GIS": 0.72,
        "K": 0.73,
        "CPB": 0.71,
        "HSY": 0.72,
        "CAG": 0.71,
        "HRL": 0.72,
        "CLX": 0.73,
        "EL": 0.73,
        "MKC": 0.72,
        "TAP": 0.71,
        "TSN": 0.72,
        "SJM": 0.71,
        "CHD": 0.72,
        "NWL": 0.71,
        "MAT": 0.71,
        "HAS": 0.71,
        "LEVI": 0.71,
        "VFC": 0.72,
        "NKE": 0.75,
        "DIS": 0.7,
        "MCD": 0.68,
        "SBUX": 0.73,
        "MO": 0.7,
        "PM": 0.72,
        "BUD": 0.75,
        "DEO": 0.75,
        "BF.B": 0.72,
        "STZ": 0.73,
        "KDP": 0.71,
        "SAM": 0.71,
        "COTY": 0.71,
        "REV": 0.71,
        "JNJ": 0.78
    }

    # Dictionary of ticker to risk rating from morningstar
    energy_to_risk_rating = {
        "XOM": 4,
        "CVX": 4,
        "COP": 4,
        "EOG": 3,
        "OXY": 3,
        "PSX": 3,
        "MPC": 4,
        "VLO": 3,
        "HES": 4,
        "DVN": 4,
        "PXD": 4,
        "APA": 4,
        "NBL": 4,
        "MRO": 4,
        "NEE": 3,
        "DUK": 3,
        "SO": 3,
        "D": 3,
        "EXC": 3,
        "AEP": 3,
        "PCG": 3,
        "XEL": 3,
        "ED": 3,
        "EIX": 3
    }
    materials_to_risk_rating = {
        "BHP": 3,
        "RIO": 4,
        "ECL": 3,
        "DD": 4,
        "FCX": 4,
        "LIN": 4,
        "NEM": 3,
        "GOLD": 4,
        "NTR": 4,
        "VALE": 3,
        "AAL": 3,
        "SCCO": 3,
        "MOS": 3,
        "NCM": 3,
        "WPM": 3,
        "TECK": 4,
        "AEM": 3,
        "NUE": 3,
        "MT": 3,
        "PKX": 3,
        "ALB": 3,
        "PPG": 3,
        "CF": 3,
        "EMN": 3,
        "APD": 3,
        "FNV": 3,
        "RS": 3,
        "FMG": 3
    }
    industrial_to_risk_rating = {
        "GE": 3,
        "HON": 4,
        "MMM": 3,
        "CAT": 4,
        "BA": 4,
        "UTX": 4,
        "UNP": 3,
        "DE": 4,
        "RTX": 4,
        "LMT": 3,
        "EMR": 3,
        "ITW": 4,
        "SIEGY": 4,
        "UPS": 3,
        "GD": 3,
        "NOC": 3,
        "WM": 3,
        "AL": 3,
        "CMI": 4,
        "ABB": 3,
        "ROK": 3,
        "SBGSY": 3,
        "CSX": 3,
        "ETN": 3,
        "PH": 4,
        "PCP": 4,
        "TXT": 3
    }
    consumer_discretionary_to_risk_rating = {
        "AMZN": 3,
        "TSLA": 5,
        "DIS": 3,
        "NKE": 4,
        "HD": 3,
        "MCD": 3,
        "SBUX": 3,
        "BKNG": 3,
        "LOW": 3,
        "TGT": 3,
        "CMCSA": 3,
        "TJX": 3,
        "NFLX": 4,
        "LVMUY": 4,
        "VWAGY": 4,
        "YUM": 3,
        "KO": 3,
        "GM": 3,
        "RACE": 4,
        "PDD": 4,
        "ADDYY": 3,
        "MAR": 3,
        "HLT": 3,
        "AAL": 3,
        "CCL": 3
    }
    consumer_staples_to_risk_rating = {
        "PG": 4,
        "KO": 4,
        "PEP": 4,
        "WMT": 4,
        "CL": 4,
        "NSRGY": 4,
        "UL": 4,
        "MDLZ": 4,
        "COST": 4,
        "MO": 4,
        "KHC": 4,
        "PM": 4,
        "KMB": 4,
        "DANOY": 4,
        "DEO": 4,
        "EL": 4,
        "ADM": 4,
        "BUD": 4,
        "HSY": 4,
        "STZ": 4,
        "KDP": 4,
        "MNST": 4,
        "GIS": 4,
        "K": 4,
        "SYY": 4,
        "TSN": 4,
        "CPB": 4,
        "MKC": 4,
        "CLX": 4,
        "CHD": 4
    }
    healthcare_to_risk_rating = {
        "JNJ": 4,
        "PFE": 3,
        "MRK": 3,
        "UNH": 3,
        "ABBV": 3,
        "AMGN": 3,
        "BMY": 3,
        "LLY": 3,
        "NVS": 3,
        "GILD": 3,
        "MDT": 3,
        "ABT": 3,
        "TMO": 3,
        "VRTX": 3,
        "AZN": 3
    }
    financials_to_risk_rating = {
        "JPM": 3,
        "BAC": 3,
        "WFC": 3,
        "V": 3,
        "MA": 3,
        "BRK.B": 3,
        "PYPL": 3,
        "C": 3,
        "GS": 3,
        "MS": 3,
        "AXP": 3,
        "USB": 3,
        "SCHW": 3,
        "BLK": 3,
        "SPGI": 3,
        "COF": 3,
        "BX": 3,
        "CB": 3,
        "MET": 3,
        "AIG": 3,
        "BK": 3,
        "AFL": 3,
        "MCO": 3,
        "HIG": 3,
        "TRV": 3,
        "DFS": 3,
        "PGR": 3,
        "MMC": 3
    }
    information_technology_to_risk_rating = {
        "AAPL": 3,
        "MSFT": 3,
        "GOOGL": 3,
        "FB": 3,
        "INTC": 3,
        "NVDA": 4,
        "TSM": 4,
        "ADBE": 4,
        "CSCO": 3,
        "CRM": 3,
        "ORCL": 3,
        "IBM": 3,
        "ACN": 3,
        "SAP": 3,
        "PYPL": 3,
        "TXN": 3,
        "AVGO": 4,
        "ASML": 4,
        "NOW": 4,
        "VMW": 3,
        "AMAT": 4,
        "QCOM": 3,
        "MU": 4,
        "HPQ": 3,
        "DELL": 3,
        "UBER": 4,
        "TWTR": 4,
        "SQ": 4,
        "ZM": 4
    }
    communication_services_to_risk_rating = {
        "GOOGL": 3,
        "FB": 3,
        "TCEHY": 4,
        "BABA": 4,
        "NFLX": 4,
        "T": 3,
        "VZ": 3,
        "CMCSA": 3,
        "CHTR": 3,
        "NTT": 3,
        "SFTBY": 4,
        "CHL": 3,
        "DTEGY": 3,
        "TMUS": 3,
        "TEF": 3,
        "VOD": 3,
        "CHU": 3,
        "BCE": 3,
        "DISH": 3,
        "TLSYY": 3,
        "ORAN": 3,
        "AMX": 3,
        "BT": 3,
        "LBTYA": 3,
        "RELIANCE": 4,
        "TU": 3,
        "RCI": 3,
        "LILA": 3
    }
    utilities_to_risk_rating = {
        "NEE": 3,
        "DUK": 3,
        "D": 3,
        "SO": 3,
        "AEP": 3,
        "EXC": 3,
        "PCG": 3,
        "XEL": 3,
        "ED": 3,
        "EIX": 3,
        "SRE": 3,
        "NGG": 3,
        "EOAN": 3,
        "ENGIY": 3,
        "ENLAY": 3,
        "CPYYY": 3,
        "PEG": 3,
        "FE": 3
    }
    real_estate_to_risk_rating = {
        "AMT": 4,
        "PLD": 4,
        "SPG": 3,
        "CCI": 4,
        "EQIX": 4,
        "AVB": 3,
        "PSA": 3,
        "DLR": 3,
        "O": 3,
        "WELL": 3,
        "ESS": 3,
        "ARE": 3,
        "VTR": 3,
        "BXP": 3,
        "WY": 3,
        "PEAK": 3,
        "DRE": 3,
        "EXR": 3,
        "HST": 3,
        "VICI": 3,
        "SBAC": 3,
        "VNO": 3,
        "FRT": 3,
        "MAA": 3,
        "IRM": 3,
        "INVH": 3
    }
    consumer_goods_to_risk_rating = {
        "KO": 3,
        "PEP": 3,
        "NSRGY": 3,
        "PG": 3,
        "UL": 3,
        "KHC": 3,
        "MDLZ": 3,
        "CL": 3,
        "KMB": 3,
        "GIS": 3,
        "K": 3,
        "CPB": 3,
        "HSY": 3,
        "CAG": 3,
        "HRL": 3,
        "CLX": 3,
        "EL": 3,
        "MKC": 3,
        "TAP": 3,
        "TSN": 3,
        "SJM": 3,
        "CHD": 3,
        "NWL": 3,
        "MAT": 3,
        "HAS": 3,
        "LEVI": 3,
        "VFC": 3,
        "NKE": 3,
        "DIS": 3,
        "MCD": 3,
        "SBUX": 3,
        "MO": 3,
        "PM": 3,
        "BUD": 3,
        "DEO": 3,
        "BF.B": 3,
        "STZ": 3,
        "KDP": 3,
        "SAM": 3,
        "COTY": 3,
        "REV": 3,
        "JNJ": 3
    }

    companies_in_sector = None
    company_to_environmental_impact = None
    company_to_risk_rating = None
    if input_sector == "energy":
        companies_in_sector = energy_companies
        company_to_environmental_impact = energy_to_environmental_impact
        company_to_risk_rating = energy_to_risk_rating
    elif input_sector == "materials":
        companies_in_sector = materials_companies
        company_to_environmental_impact = materials_to_environmental_impact
        company_to_risk_rating = materials_to_risk_rating
    elif input_sector == "industrial":
        companies_in_sector = industrial_companies
        company_to_environmental_impact = industrial_to_environmental_impact
        company_to_risk_rating = industrial_to_risk_rating
    elif input_sector == "consumer_discretionary":
        companies_in_sector = consumer_discretionary_companies
        company_to_environmental_impact = consumer_discretionary_to_environmental_impact
        company_to_risk_rating = consumer_discretionary_to_risk_rating
    elif input_sector == "consumer_staples":
        companies_in_sector = consumer_staples_companies
        company_to_environmental_impact = consumer_staples_to_environmental_impact
        company_to_risk_rating = consumer_staples_to_risk_rating
    elif input_sector == "healthcare":
        companies_in_sector = healthcare_companies
        company_to_environmental_impact = healthcare_to_environmental_impact
        company_to_risk_rating = healthcare_to_risk_rating
    elif input_sector == "financials":
        companies_in_sector = financials_companies
        company_to_environmental_impact = financials_to_environmental_impact
        company_to_risk_rating = financials_to_risk_rating
    elif input_sector == "information_technology":
        companies_in_sector = information_technology_companies
        company_to_environmental_impact = information_technology_to_environmental_impact
        company_to_risk_rating = information_technology_to_risk_rating
    elif input_sector == "communication_services":
        companies_in_sector = communication_services_companies
        company_to_environmental_impact = communication_services_to_environmental_impact
        company_to_risk_rating = communication_services_to_risk_rating
    elif input_sector == "utilities":
        companies_in_sector = utilities_companies
        company_to_environmental_impact = utilities_to_environmental_impact
        company_to_risk_rating = utilities_to_risk_rating
    elif input_sector == "real_estate":
        companies_in_sector = real_estate_companies
        company_to_environmental_impact = real_estate_to_environmental_impact
        company_to_risk_rating = real_estate_to_risk_rating
    elif input_sector == "consumer_goods":
        companies_in_sector = consumer_goods_companies
        company_to_environmental_impact = consumer_goods_to_environmental_impact
        company_to_risk_rating = consumer_goods_to_risk_rating

    sector_of_input_companyLst = [sector for (sector,companies) in ticker_sector.items() if input_company in companies]
    if sector_of_input_companyLst:
        sector_of_input_company = sector_of_input_companyLst[0]
    else:
        sector_of_input_company = ""
    
    risk_of_input_company = None
    if sector_of_input_company == "energy":
        risk_of_input_company = energy_to_risk_rating[input_company]
    elif sector_of_input_company == "materials":
        risk_of_input_company = materials_to_risk_rating[input_company]
    elif sector_of_input_company == "industrial":
        risk_of_input_company = industrial_to_risk_rating[input_company]
    elif sector_of_input_company == "consumer_discretionary":
        risk_of_input_company = consumer_discretionary_to_risk_rating[input_company]
    elif sector_of_input_company == "consumer_staples":
        risk_of_input_company = consumer_staples_to_risk_rating[input_company]
    elif sector_of_input_company == "healthcare":
        risk_of_input_company = healthcare_to_risk_rating[input_company]
    elif sector_of_input_company == "financials":
        risk_of_input_company = financials_to_risk_rating[input_company]
    elif sector_of_input_company == "information_technology":
        risk_of_input_company = information_technology_to_risk_rating[input_company]
    elif sector_of_input_company == "communication_services":
        risk_of_input_company = communication_services_to_risk_rating[input_company]
    elif sector_of_input_company == "utilities":
        risk_of_input_company = utilities_to_risk_rating[input_company]
    elif sector_of_input_company == "real_estate":
        risk_of_input_company = real_estate_to_risk_rating[input_company]
    elif sector_of_input_company == "consumer_goods":
        risk_of_input_company = consumer_goods_to_risk_rating[input_company]


    input_risk_rating = int(input_risk_rating or risk_of_input_company or 3)  # Assume risk of 3 if data not available
    all_recommendations, recommended_company = recommend_similar_company(input_company, input_sector, input_risk_rating, companies_in_sector, company_to_environmental_impact, company_to_risk_rating)
    if num_wanted:
        top_recommendations = dict(sorted(all_recommendations.items(), key=lambda item: item[1], reverse=True)[:int(num_wanted)])
    else:
        top_recommendations = dict(sorted(all_recommendations.items(), key=lambda item: item[1], reverse=True)[:5])

    top_recs_with_eco = {company : (score, company_to_environmental_impact[company]) for (company, score) in top_recommendations.items()}

    return top_recs_with_eco

app.debug = True
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
