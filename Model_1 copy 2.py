import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import warnings
warnings.filterwarnings("ignore", message="The 'unit' keyword in TimedeltaIndex construction is deprecated.*")
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def stock_symbols():
    nifty_200_symbols = ['ITC.NS', 'TITAN.NS','TECHM.NS','RITES.NS','ULTRACEMCO.NS','MARUTI.NS','BAJFINANCE.NS','COALINDIA.NS',
                         'APOLLOHOSP.NS','HDFCLIFE.NS','MAHSEAMLES.NS','RELIANCE.NS','TCS.NS','HDFCBANK.NS','ICICIBANK.NS','INFY.NS',
                         'BHARTIARTL.NS','HINDUNILVR.NS','SBIN.NS','LICI.NS','HCLTECH.NS','KOTAKBANK.NS','ADANIENT.NS','AXISBANK.NS',
                         'SUNPHARMA.NS','ASIANPAINT.NS','NTPC.NS','TATAMOTORS.NS','ONGC.NS','ADANIGREEN.NS','BAJAJFINSV.NS','ADANIPORTS.NS',
                         'DMART.NS','NESTLEIND.NS','WIPRO.NS','POWERGRID.NS','ADANIPOWER.NS','BAJAJ-AUTO.NS','M&M.NS','HAL.NS','DLF.NS',
                         'IOC.NS','LTIM.NS','TATASTEEL.NS','SIEMENS.NS','SBILIFE.NS','GRASIM.NS','PIDILITIND.NS','BEL.NS','HINDZINC.NS',
                         'PFC.NS','INDUSINDBK.NS','ADANIENSOL.NS','BRITANNIA.NS','HINDALCO.NS','ZOMATO.NS','BANKBARODA.NS','INDIGO.NS',
                         'GODREJCP.NS','LODHA.NS','ATGL.NS','TATAPOWER.NS','TRENT.NS','RECLTD.NS','TATACONSUM.NS','PNB.NS','CIPLA.NS',
                         'AMBUJACEM.NS','GAIL.NS','EICHERMOT.NS','DIVISLAB.NS','ABB.NS','VEDL.NS','TVSMOTOR.NS','BPCL.NS','DABUR.NS',
                         'UNIONBANK.NS','SHREECEM.NS','DRREDDY.NS','HAVELLS.NS','ABB.BO','ALKEM.BO','ASHOKLEY.BO','AUBANK.BO','AUROPHARMA.BO',
                         'BAJAJHLDNG.BO','BALKRISHNA.BO','BANKINDIA.BO','BERGEPAINT.BO','BHARATFORG.BO','BHEL.BO','BOSCHLTD.BO','BPCL.BO',
                         'CANBK.BO','CGPOWER.BO','CHOLAFIN.BO','CIPLA.BO','COLPAL.BO','CONCOR.BO','CUMMINSIND.BO','DIVISLAB.BO','FACT.BO',
                         'DRREDDY.BO','EICHERMOT.BO','GICRE.BO','GMRINFRA.BO','HDFCAMC.BO','GODREJPROP.BO','HEROMOTOCO.BO','HINDALCO.BO',
                         'HINDPETRO.BO','HINDUNILVR.BO','HINDZINC.BO','ICICIBANK.BO','ICICIGI.BO','IDBI.BO','IDEA.BO','IDFCFIRSTB.BO',
                         'INDHOTEL.BO','INDIANB.BO','INDIGO.BO','INDUSINDBK.BO','INDUSTOWER.BO','IOB.BO','IRCTC.BO','IRFC.BO','JINDALSTEL.BO',
                         'JIOFIN.BO','JSWENERGY.BO','JSWSTEEL.BO','KOTAKBANK.BO','LICI.BO','LT.BO','LTIM.BO','LTTS.BO','LUPIN.BO','M&M.BO',
                         'MANKIND.BO','MARICO.BO','MAXHEALTH.BO','MOTHERSON.BO','MRF.BO','MUTHOOTFIN.BO','NAUKRI.BO','NESTLEIND.BO','NHPC.BO',
                         'NMDC.BO','NTPC.BO','OBEROIRLTY.BO','OFSS.BO','ONGC.BO','PATANJALI.BO','PERSISTENT.BO','PFC.BO','PGHH.BO',
                         'PIDILITIND.BO','PIIND.BO','PNB.BO','POLYCAB.BO','POWERGRID.BO','RECLTD.BO','RVNL.BO','SAIL.BO','SBICARD.BO',
                         'SBILIFE.BO','SHREECEM.BO','SHRIRAMFIN.BO','SIEMENS.BO','SJVN.BO','SOLARINDS.BO','SRF.BO','SUNPHARMA.BO',
                         'SUPREMEIND.BO','SUZLON.BO','TATACONSUM.BO','TATAMOTORS.BO','TATAMTRDVR.BO','TATAPOWER.BO','TATASTEEL.BO',
                         'TIINDIA.BO','TITAN.BO','TORNTPOWER.BO','TVSMOTOR.BO','UCOBANK.BO','ULTRACEMCO.BO','UNIONBANK.BO','VBL.BO','VEDL.BO',
                         'WIPRO.BO','YESBANK.BO','ZOMATO.BO','ZYDUSLIFE.BO','TORNTPHARM.NS','ICICIPRULI.BO','ABBOTINDIA.NS','CENTRALBK.NS',
                         'ASTRAL.NS','JSL.NS','JSWINFRA.NS','MUTHOOTFIN.NS','TATACOMM.NS','PHOENIXLTD.BO','MPHASIS.NS','FACT.NS','ACC.NS',
                         'SUPREMEIND.NS','AWL.NS','PRESTIGE.NS','TATAELXSI.NS','SJVN.NS','LINDEINDIA.NS','TATATECH.NS','POLICYBZR.BO',
                         'SUNDARMFIN.BO','NIACL.BO','SCHAEFFLER.BO','UBL.BO','BALKRISIND.BO','PSB.BO','MRPL.BO','MAHABANK.BO','NYKAA.BO',
                         'PETRONET.BO','KPITTECH.BO','L&TFH.BO','IREDA.BO','MAZDOCK.BO','THERMAX.BO','COFORGE.BO','DIXON.BO','IRB.BO',
                         'HUDCO.BO','AUBANK.BO','DALBHARAT.BO','MEDANTA.BO','KALYANKJIL.BO','GUJGASLTD.BO','UNOMINDA.BO','FEDERALBNK.BO',
                         'UNITDSPR.BO','GLAXO.BO','POONAWALLA.BO','VOLTAS.BO','UPL.BO','TATAINVEST.BO','CRISIL.BO','M&MFIN.BO','LICHSGFIN.BO',
                         'AIAENG.BO','3MINDIA.BO','JKCEMENT.BO','EMBASSY.BO','DELHIVERY.BO','BDL.BO','HONAUT.BO','STARHEALTH.BO','NAM-INDIA.BO',
                         'BIOCON.BO','APOLLOTYRE.BO','FORTIS.BO','BANDHANBNK.BO','NLCINDIA.BO','MFSL.BO','JUBLFOOD.BO','MSUMI.BO','ESCORTS.BO',
                         'DEEPAKNTR.BO','METROBRAND.BO','KEI.BO','IGL.BO','IPCALAB.BO','DEEPAKNTR.BO','FORTIS.BO','NATIONALUM.BO','MSUMI.BO',
                         'LLOYDSME.BO','JUBLFOOD.BO','GLAND.BO','EXIDEIND.BO','POWERINDIA.BO','SYNGENE.BO','GODREJIND.BO','KIOCL.BO',
                         'BLUESTARCO.BO','KPRMILL.BO','ZFCVINDIA.BO','HINDCOPPER.BO','ITI.BO','GLENMARK.BO','EIHOTEL.BO','AJANTPHARM.BO',
                         'ENDURANCE.BO','ISEC.BO','HATSUN.BO','JBCHEPHARM.BO','BAYERCROP.BO','GET&D.BO','SUNTV.BO','APARINDS.BO','360ONE.BO',
                         'NH.BO','AARTIIND.BO','MOTILALOFS.BO','MANYAVAR.BO','KANSAINER.BO','ANGELONE.BO','NBCC.BO','COCHINSHIP.BO','ABFRL.BO',
                         'LAURUSLABS.BO','GRINDWELL.BO','JBMA.BO','CREDITACC.BO','ASTERDM.BO','ELGIEQUIP.BO','SONATSOFTW.BO','RADICO.BO',
                         'CARBORUNIV.BO','SKFINDIA.BO','CHOLAHLDNG.BO','RELAXO.BO','CASTROLIND.BO','MINDSPACE.BO','GSPL.BO','ELGIEQUIP.BO',
                         'BRIGADE.BO','PFIZER.BO','KAJARIACER.BO','IRCON.BO','EMAMILTD.BO','PEL.BO','APLLTD.BO','TRIDENT.BO','SANOFI.BO',
                         'RAMCOCEM.BO','FIVESTAR.BO','TIMKEN.BO','SIGNATURE.BO','RATNAMANI.BO','KEC.BO','CROMPTON.BO','BATAINDIA.BO','KAYNES.BO',
                         'DEVYANI.BO','IDFC.BO','ATUL.BO','JAIBALAJI.BO','MCX.BO','LALPATHLAB.BO','TVSHLTD.BO','SUMICHEM.BO','NATCOPHARM.BO',
                         'KPIL.BO','NSLNISP.BO','PNBHOUSING.BO','SWANENERGY.BO','GODFRYPHLP.BO','CIEINDIA.BO','SUVENPHAR.BO','APTUS.BO','CELLO.BO',
                         'VINATIORGA.BO','KIMS.BO','MCX.BO','CIEINDIA.BO','SWANENERGY.BO','SUVENPHAR.BO','REDINGTON.BO','INTELLECT.BO','WHIRLPOOL.BO',
                         'NSLNISP.BO','CENTURYTEX.BO','RRKABEL.BO','APTUS.BO','GODFRYPHLP.BO','TTML.BO','PPLPHARMA.BO','ANANDRATHI.BO','INDIAMART.BO',
                         'JYOTHYLAB.BO','CESC.BO','SHYAMMETL.BO','ACE.BO','SCHNEIDER.BO','LAXMIMACH.BO','INOXWIND.BO','CHALET.BO','ARE&M.BO',
                         'IIFL.BO','ZEEL.BO','RBLBANK.BO','CGCL.BO','NCC.BO','TRITURBINE.BO','LAXMIMACH.BO','NAVINFLUOR.BO','HSCL.BO',
                         'INOXWIND.BO','CHALET.BO','OLECTRA.BO','ARE&M.BO','CONCORDBIO.BO','AFFLE.BO','KARURVYSYA.BO','WELSPUNLIV.BO',
                         'NUVAMA.BO','BLS.BO','VGUARD.BO','CAMS.BO','MANAPPURAM.BO','ABSLAMC.BO','JWL.BO','BASF.BO','ALOKINDS.BO',
                         'CHAMBLFERT.BO','GESHIP.BO','CLEAN.BO','RBLBANK.BO','POLYMED.BO','BLUEDART.BO','DCMSHRIRAM.BO','JINDALSAW.BO',
                         'WELCORP.BO','DATAPATTNS.BO','FSL.BO','J&KBANK.BO','FINPIPE.BO','HFCL.BO','PVRINOX.BO','FINCABLES.BO','CHENNPETRO.BO',
                         'ASAHIINDIA.BO','MGL.BO','ZENSARTECH.BO','FINEORG.BO','BIKAJI.BO','HONASA.BO','SOBHA.BO','ASTRAZEN.BO','VTL.BO',
                         'IEX.BO','HBLPOWER.BO','KSB.BO','TEJASNET.BO','TITAGARH.BO','MAHSEAMLES.BO','HAPPSTMNDS.BO','GRAPHITE.BO',
                         'INGERRAND.BO','GRINFRA.BO','AMBER.BO','SPLPETRO.BO','ECLERX.BO','ERIS.BO','TANLA.BO','SWSOLAR.BO','DBREALTY.BO',
                         'BEML.BO','WESTLIFE.BO','SPARC.BO','PTCIL.BO','KIRLOSENG.BO','BBTC.BO','RAINBOW.BO','JKTYRE.BO','RKFORGE.BO',
                         'RAYMOND.BO','BAJAJELEC.BO','GMDCLTD.BO','ENGINERSIN.BO','BIRLACORPN.BO','AAVAS.BO','RAILTEL.BO','UTIAMC.BO',
                         'SANDUMA.BO','NUVOCO.BO','RHIM.BO','BIRET.BO','JPPOWER.BO','SFL.BO','INOXINDIA.BO','AKZOINDIA.BO','EQUITASBNK.BO',
                         'IBULHSGFIN.BO','AETHER.BO','PNCINFRA.BO','INFIBEAM.BO','MMTC.BO','INDIGRID.BO','NEWGEN.BO','GRANULES.BO',
                         'ANANTRAJ.BO','ANURAS.BO','CEATLTD.BO','LEMONTREE.BO','KFINTECH.BO','ALKYLAMINE.BO','RTNINDIA.BO','EIDPARRY.BO',
                         'IFCI.BO','ROUTE.BO','TTKPRESTIG.BO','CANFINHOME.BO','CAPLIPOINT.BO','JKLAKSHMI.BO','GODREJAGRO.BO','CUB.BO',
                         'PCBL.BO','SCI.BO','ELECON.BO','UJJIVANSFB.BO','ZYDUSWELL.BO','LATENTVIEW.BO','GPIL.BO','CERA.BO','RATEGAIN.BO',
                         'ELECTCAST.BO','GNFC.BO','MAPMYINDIA.BO','KPIGREEN.BO','JUBLPHARMA.BO','GPPL.BO','MINDACORP.BO','RENUKA.BO',
                         'GLS.BO','USHAMART.BO','NETWORK18.BO']  # Replace with actual symbols


    # nifty_200_symbols = ['ITC.NS', 'TITAN.NS','TECHM.NS','RITES.NS','ULTRACEMCO.NS','MARUTI.NS','BAJFINANCE.NS','COALINDIA.NS',
    #                      'APOLLOHOSP.NS','HDFCLIFE.NS','MAHSEAMLES.NS','RELIANCE.NS','TCS.NS','HDFCBANK.NS','ICICIBANK.NS','INFY.NS',
    #                      'BHARTIARTL.NS','HINDUNILVR.NS','SBIN.NS','LICI.NS','HCLTECH.NS','KOTAKBANK.NS','ADANIENT.NS','AXISBANK.NS',
    #                      'SUNPHARMA.NS','ASIANPAINT.NS','NTPC.NS','TATAMOTORS.NS','ONGC.NS','ADANIGREEN.NS','BAJAJFINSV.NS','ADANIPORTS.NS',
    #                      'DMART.NS','NESTLEIND.NS','WIPRO.NS','POWERGRID.NS','ADANIPOWER.NS','BAJAJ-AUTO.NS','M&M.NS','HAL.NS','DLF.NS',
    #                      'IOC.NS','LTIM.NS','TATASTEEL.NS','SIEMENS.NS','SBILIFE.NS','GRASIM.NS','PIDILITIND.NS','BEL.NS','HINDZINC.NS']  # Repl
    
    return nifty_200_symbols
Stocks = []
# ------------------------------------------------------------------------------------------------------------------------------------------------
def send_email(subject, body):
    sender_email = "criobd.rites@gmail.com"
    sender_password = "eqhl qvmp ruaz jrlk"
    receiver_email = ["sumitkrrajput1@gmail.com", "ntn.rajput89@gmail.com", "shankarshanky1982@gmail.com"]

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ','.join(receiver_email)
    msg['Subject'] = subject

    # Attach the body of the email
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Setup the server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Login to your Gmail account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())

        # Quit the server
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
# ------------------------------------------------------------------------------------------------------------------------------------------------
def merge_levels_up(array, tolerance_percentage=2):
    array = array.to_numpy()
    sorted_array = sorted(array)
    sorted_array.sort(reverse=True)
    result = [sorted_array[0]]  # Initialize result with the first element

    for i in range(1, len(sorted_array)):
        current_number = sorted_array[i]
        previous_number = result[-1]

        # Check if the current number is more than 5% greater than the previous number
        if current_number < previous_number * (1 - tolerance_percentage / 100):
            result.append(current_number)
    return result
# ------------------------------------------------------------------------------------------------------------------------------------------------
def merge_levels_down(array, tolerance_percentage=2):

    array = array.to_numpy()
    sorted_array = sorted(array)
    sorted_array.sort()
    result = [sorted_array[0]]  # Initialize result with the first element

    for i in range(1, len(sorted_array)):
        current_number = sorted_array[i]
        previous_number = result[-1]

        # Check if the current number is more than 5% greater than the previous number
        if current_number > previous_number * (1 + tolerance_percentage / 100):
            result.append(current_number)
    return result
# ------------------------------------------------------------------------------------------------------------------------------------------------
def get_max (reversal_points, tolerance_percentage = 1 ):
    all_levels = reversal_points['Close']
    imp_levels = []
   
    used_level = set()

    for level in all_levels:
        if level not in used_level:
            lower_bound = level * (1-(tolerance_percentage/100))  # 1% lower
            upper_bound = level * (1+(tolerance_percentage/100))
            filtered_df = reversal_points[(reversal_points['Close'] >= lower_bound) & (reversal_points['Close'] <= upper_bound)]
            
            count = len(filtered_df)
            
            average_value = filtered_df['Close'].mean()
            imp_levels.append({'Level': average_value, 'Count': count})
            used_level.update(filtered_df['Close'])
                
    df_level_set1 = pd.DataFrame(imp_levels)

    result_df = df_level_set1.copy()
    used_values = set()
    final_levels = []

    for index, row in result_df.iterrows():
        if row['Level'] not in used_values:
            
            lower_bound = row['Level'] * (1 - (tolerance_percentage / 100))  # 1% lower
            upper_bound = row['Level'] * (1 + (tolerance_percentage / 100))
            filtered_df = result_df[(result_df['Level'] >= lower_bound) & (result_df['Level'] <= upper_bound)]
            count_sum = filtered_df['Count'].sum()
            average_value = filtered_df['Level'].mean()
            final_levels.append({'Level': average_value, 'Count': count_sum})
            result_df.loc[index, 'Sum_Count'] = count_sum
            used_values.update(filtered_df['Level'])

    df_maximums = pd.DataFrame(final_levels)
    print(df_maximums)
    return df_maximums
       
    return df_maximums
# ------------------------------------------------------------------------------------------------------------------------------------------------
def check_level_1(symbol, parso_price, previous_day_price, current_price, ma_20, ma_50, ma_200, delta, delta_high, delta_low, today_3_4, imp_levels_max):
    
    if current_price > previous_day_price and ma_20 > ma_50 and ma_50 > ma_200 and delta > 0 and current_price > today_3_4 and delta_high > 0 and delta_low > 0:
      
      check_level_crossing(imp_levels_max,current_price,previous_day_price,parso_price,symbol,all_high,ma_20, ma_50, ma_200)
# ------------------------------------------------------------------------------------------------------------------------------------------------
def check_level_crossing(imp_levels_max,current_price,previous_day_price,parso_price,symbol,all_high,ma_20,ma_50,ma_200):
    global Stocks


    for i in range (len(imp_levels_max)-1):
      near_high = 0
      levels = imp_levels_max[i]
      if i > 0 and i< (len(imp_levels_max)-1) :
        nxt_level = imp_levels_max[i-1]
        lower_level = imp_levels_max[i+1]
      # if i == (len(imp_levels_max)-1):
      if(i==0):
        near_high = 1
        lower_level = imp_levels_max[i+1]
        

      if ((previous_day_price <  levels) and (current_price > levels) ) or ((parso_price > previous_day_price) and (previous_day_price < 1.01* levels) and (current_price > levels)):

       

        if(current_price < 1.05 * ma_20 ) and (ma_20 > 1.10 * ma_50) and (levels < 1.01 * ma_20):
            print("1","time to Buy ma 20", symbol, 'for crossing', levels)
            print('symbol',symbol,parso_price,previous_day_price,current_price)
            print(imp_levels_max)
            Stocks.append([symbol,"ma 20",levels])

        if (near_high == 1) and (current_price < 1.02 * levels) and (all_high > 1.09  * current_price)  :
            print(all_high)
            print("2","time to Buy  near high", symbol, 'for crossing', levels)
            print(imp_levels_max)
            Stocks.append([symbol,"High",levels])

        if (near_high == 0 ) and (nxt_level > 1.07*levels) and (lower_level > 0.95 * levels) and (nxt_level > 1.05 * current_price):
            print("3","time to Buy", symbol, 'for crossing', levels, 'next level:',nxt_level)
            print(imp_levels_max)
            Stocks.append([symbol,levels])
# ------------------------------------------------------------------------------------------------------------------------------------------------
# nifty_200_symbols = stock_symbols()
nifty_200_symbols = ['COALINDIA.NS','RITES.NS']
# ------------------------------------------------------------------------------------------------------------------------------------------------
# Specify the date range for the historical data (5 years ago from today)
end_date = datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.today() - timedelta(days=5*365)).strftime('%Y-%m-%d')
# Create an empty DataFrame to store the data
nifty_200_data = pd.DataFrame()
# Fetch historical data for each stock and making data frame (Multiple Rows---> Row 1 to 500 : Stock1, Row 501 to 1000 : Stock 2 .... So on)
# ------------------------------------------------------------------------------------------------------------------------------------------------
for symbol in nifty_200_symbols:
    try:
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        stock_data = stock_data.reset_index()  # Reset index to have 'Date' as a column
        stock_data['Symbol'] = symbol  # Add a column for stock symbol
        stock_data = stock_data[['Symbol', 'Date', 'Close', 'Open','Low','High']]
        nifty_200_data = pd.concat([nifty_200_data, stock_data])
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")

for symbol in nifty_200_symbols:
    itc_data = nifty_200_data[nifty_200_data['Symbol'] == symbol]
    share_details = yf.Ticker(symbol)
    share_history = share_details.history()

    current_price = share_history['Close'].iloc[-1]
    open_price = share_history['Open'].iloc[-1]
    previous_day_price = share_history['Close'].iloc[-2]
    parso_price = share_history['Close'].iloc[-3]
    all_high = max(itc_data['Close'])

    delta_high = (share_history['High'].iloc[-1])-(share_history['High'].iloc[-2]) #difference between high of today and yesterday
    delta_low = (share_history['Low'].iloc[-1])-(share_history['Low'].iloc[-2]) #difference between lows of today and yesterday

    today_3_4 = (share_history['Low'].iloc[-1]) + (0.75* (share_history['High'].iloc[-1]  - share_history['Low'].iloc[-1]))  # 3/4 th of the todays low

    ma_20= itc_data['Close'].tail(20).mean()
    ma_50= itc_data['Close'].tail(50).mean()
    ma_200 = itc_data['Close'].tail(200).mean()

    Week_Stock = itc_data.copy()

    Week_Stock['Date'] = pd.to_datetime(Week_Stock['Date'])
    Week_Stock.set_index('Date', inplace=True)
    W_S_Grouped = Week_Stock.groupby('Symbol').resample('W')
    weekly_data = W_S_Grouped.agg({ 'Open': 'first','Close': 'last', 'High': 'max','Low': 'min'}).reset_index()
    weekly_data.columns = ['stock_symbol', 'Date', 'open_price_week', 'Close', 'high_price_week', 'low_price_week']

    weekly_data['ha_Close'] = (weekly_data['open_price_week'] + weekly_data['high_price_week'] + weekly_data['low_price_week'] + weekly_data['Close']) / 4
    weekly_data['Change'] = weekly_data['ha_Close'].diff().apply(lambda x: 'Increased' if x > 0 else 'Decreased')
    weekly_data['Sign Change'] = weekly_data['Change'] != weekly_data['Change'].shift(1)
    W_slope_change_points = weekly_data[weekly_data['Sign Change']]
    W_rows_with_sign_change = weekly_data[weekly_data['Sign Change']].index.to_numpy()
    W_rows_with_sign_change[1:] -= 1
    W_reversal_points = weekly_data.iloc[W_rows_with_sign_change]
    # print(weekly_data)

    delta = current_price - open_price

    reversal_points = weekly_data.iloc[W_rows_with_sign_change]
    print(reversal_points)
    df_maximums = get_max(reversal_points)
    
    imp_levels_max = merge_levels_up(df_maximums['Level'])

    print(imp_levels_max)

    # plt.figure(figsize=(10, 6))
    # # plt.plot(df_maximums['Date'], df_maximums['Maximums'], marker='o', label='Maximums')
    # # plt.plot(df_minimums['Date'], df_minimums['Minimums'], marker='x', label='Minimums')
    # plt.plot(itc_data['Date'], itc_data['Close'], marker='', label='Close')
    # for level in imp_levels_max:
    #     plt.axhline(y=level, linestyle='--', label=f'Level {level}')
    # # for level in imp_levels_min:
    # #     plt.axhline(y=level, linestyle=':', label=f'Level {level}')
    # plt.title('Graph of Maximums Over Time')
    # plt.xlabel('Date')
    # plt.ylabel('Maximums')
    # plt.legend()
    # plt.grid(True)
    # plt.show()

    check_level_1(symbol, parso_price, previous_day_price, current_price, ma_20, ma_50, ma_200, delta, delta_high, delta_low, today_3_4, imp_levels_max)
    
Shares = ' & '.join([' '.join(map(str, inner_list)) for inner_list in Stocks])
# send_email('Swing Tip', Shares)
