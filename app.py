{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, request, render_template\n",
    "from flask_cors import cross_origin\n",
    "import sklearn\n",
    "import pickle\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting Flask-Cors==1.10.3\n",
      "  Downloading Flask-Cors-1.10.3.tar.gz (28 kB)\n",
      "Requirement already satisfied: Flask>=0.9 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from Flask-Cors==1.10.3) (1.1.2)\n",
      "Requirement already satisfied: Six in c:\\users\\hp\\anaconda3\\lib\\site-packages (from Flask-Cors==1.10.3) (1.15.0)\n",
      "Requirement already satisfied: Werkzeug>=0.15 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from Flask>=0.9->Flask-Cors==1.10.3) (1.0.1)\n",
      "Requirement already satisfied: itsdangerous>=0.24 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from Flask>=0.9->Flask-Cors==1.10.3) (1.1.0)\n",
      "Requirement already satisfied: Jinja2>=2.10.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from Flask>=0.9->Flask-Cors==1.10.3) (2.11.2)\n",
      "Requirement already satisfied: click>=5.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from Flask>=0.9->Flask-Cors==1.10.3) (7.1.2)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from Jinja2>=2.10.1->Flask>=0.9->Flask-Cors==1.10.3) (1.1.1)\n",
      "Building wheels for collected packages: Flask-Cors\n",
      "  Building wheel for Flask-Cors (setup.py): started\n",
      "  Building wheel for Flask-Cors (setup.py): finished with status 'done'\n",
      "  Created wheel for Flask-Cors: filename=Flask_Cors-1.10.3-py3-none-any.whl size=11537 sha256=fbec7781741d8508ea9e4fb1d37400aad4e9a628b25a5dbffb9458e40e8ae3ee\n",
      "  Stored in directory: c:\\users\\hp\\appdata\\local\\pip\\cache\\wheels\\03\\db\\16\\6eb82efe1cdfd995071d47100c6c5ffda40c28d1edf9c9365b\n",
      "Successfully built Flask-Cors\n",
      "Installing collected packages: Flask-Cors\n",
      "Successfully installed Flask-Cors-1.10.3\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install Flask-Cors==1.10.3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)\n",
    "model = pickle.load(open('flight_rf.pkl', 'rb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/')\n",
    "@cross_origin()\n",
    "def home():\n",
    "    return render_template('home.html')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "__init__() got an unexpected keyword argument 'method'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-8-5eb611d7051a>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;33m@\u001b[0m\u001b[0mapp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mroute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'/predict'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmethod\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;34m'GET'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'POST'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;33m@\u001b[0m\u001b[0mcross_origin\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[1;32mdef\u001b[0m \u001b[0mpredict\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mrequest\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmethod\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m\"POST\"\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\flask\\app.py\u001b[0m in \u001b[0;36mdecorator\u001b[1;34m(f)\u001b[0m\n\u001b[0;32m   1313\u001b[0m         \u001b[1;32mdef\u001b[0m \u001b[0mdecorator\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mf\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1314\u001b[0m             \u001b[0mendpoint\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0moptions\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpop\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"endpoint\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1315\u001b[1;33m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0madd_url_rule\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mrule\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mendpoint\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0moptions\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1316\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1317\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\flask\\app.py\u001b[0m in \u001b[0;36mwrapper_func\u001b[1;34m(self, *args, **kwargs)\u001b[0m\n\u001b[0;32m     96\u001b[0m                 \u001b[1;34m\"before the application starts serving requests.\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     97\u001b[0m             )\n\u001b[1;32m---> 98\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     99\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    100\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mupdate_wrapper\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mwrapper_func\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\flask\\app.py\u001b[0m in \u001b[0;36madd_url_rule\u001b[1;34m(self, rule, endpoint, view_func, provide_automatic_options, **options)\u001b[0m\n\u001b[0;32m   1273\u001b[0m         \u001b[0mmethods\u001b[0m \u001b[1;33m|=\u001b[0m \u001b[0mrequired_methods\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1274\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1275\u001b[1;33m         \u001b[0mrule\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0murl_rule_class\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mrule\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmethods\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mmethods\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0moptions\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1276\u001b[0m         \u001b[0mrule\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mprovide_automatic_options\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mprovide_automatic_options\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1277\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: __init__() got an unexpected keyword argument 'method'"
     ]
    }
   ],
   "source": [
    "@app.route('/predict', method = ['GET', 'POST'])\n",
    "@cross_origin()\n",
    "def predict():\n",
    "    if request.method == \"POST\":\n",
    "\n",
    "        # Date_of_Journey\n",
    "        date_dep = request.form[\"Dep_Time\"]\n",
    "        Journey_day = int(pd.to_datetime(date_dep, format=\"%Y-%m-%dT%H:%M\").day)\n",
    "        Journey_month = int(pd.to_datetime(date_dep, format =\"%Y-%m-%dT%H:%M\").month)\n",
    "        # print(\"Journey Date : \",Journey_day, Journey_month)\n",
    "\n",
    "        # Departure\n",
    "        Dep_hour = int(pd.to_datetime(date_dep, format =\"%Y-%m-%dT%H:%M\").hour)\n",
    "        Dep_min = int(pd.to_datetime(date_dep, format =\"%Y-%m-%dT%H:%M\").minute)\n",
    "        # print(\"Departure : \",Dep_hour, Dep_min)\n",
    "\n",
    "        # Arrival\n",
    "        date_arr = request.form[\"Arrival_Time\"]\n",
    "        Arrival_hour = int(pd.to_datetime(date_arr, format =\"%Y-%m-%dT%H:%M\").hour)\n",
    "        Arrival_min = int(pd.to_datetime(date_arr, format =\"%Y-%m-%dT%H:%M\").minute)\n",
    "        # print(\"Arrival : \", Arrival_hour, Arrival_min)\n",
    "\n",
    "        # Duration\n",
    "        dur_hour = abs(Arrival_hour - Dep_hour)\n",
    "        dur_min = abs(Arrival_min - Dep_min)\n",
    "        # print(\"Duration : \", dur_hour, dur_min)\n",
    "\n",
    "        # Total Stops\n",
    "        Total_stops = int(request.form[\"stops\"])\n",
    "        # print(Total_stops)\n",
    "\n",
    "        # Airline\n",
    "        # AIR ASIA = 0 (not in column)\n",
    "        airline=request.form['airline']\n",
    "        if(airline=='Jet Airways'):\n",
    "            Jet_Airways = 1\n",
    "            IndiGo = 0\n",
    "            Air_India = 0\n",
    "            Multiple_carriers = 0\n",
    "            SpiceJet = 0\n",
    "            Vistara = 0\n",
    "            GoAir = 0\n",
    "            Multiple_carriers_Premium_economy = 0\n",
    "            Jet_Airways_Business = 0\n",
    "            Vistara_Premium_economy = 0\n",
    "            Trujet = 0 \n",
    "\n",
    "        elif (airline=='IndiGo'):\n",
    "            Jet_Airways = 0\n",
    "            IndiGo = 1\n",
    "            Air_India = 0\n",
    "            Multiple_carriers = 0\n",
    "            SpiceJet = 0\n",
    "            Vistara = 0\n",
    "            GoAir = 0\n",
    "            Multiple_carriers_Premium_economy = 0\n",
    "            Jet_Airways_Business = 0\n",
    "            Vistara_Premium_economy = 0\n",
    "            Trujet = 0 \n",
    "\n",
    "        elif (airline=='Air India'):\n",
    "            Jet_Airways = 0\n",
    "            IndiGo = 0\n",
    "            Air_India = 1\n",
    "            Multiple_carriers = 0\n",
    "            SpiceJet = 0\n",
    "            Vistara = 0\n",
    "            GoAir = 0\n",
    "            Multiple_carriers_Premium_economy = 0\n",
    "            Jet_Airways_Business = 0\n",
    "            Vistara_Premium_economy = 0\n",
    "            Trujet = 0 \n",
    "            \n",
    "        elif (airline=='Multiple carriers'):\n",
    "            Jet_Airways = 0\n",
    "            IndiGo = 0\n",
    "            Air_India = 0\n",
    "            Multiple_carriers = 1\n",
    "            SpiceJet = 0\n",
    "            Vistara = 0\n",
    "            GoAir = 0\n",
    "            Multiple_carriers_Premium_economy = 0\n",
    "            Jet_Airways_Business = 0\n",
    "            Vistara_Premium_economy = 0\n",
    "            Trujet = 0 \n",
    "            \n",
    "        elif (airline=='SpiceJet'):\n",
    "            Jet_Airways = 0\n",
    "            IndiGo = 0\n",
    "            Air_India = 0\n",
    "            Multiple_carriers = 0\n",
    "            SpiceJet = 1\n",
    "            Vistara = 0\n",
    "            GoAir = 0\n",
    "            Multiple_carriers_Premium_economy = 0\n",
    "            Jet_Airways_Business = 0\n",
    "            Vistara_Premium_economy = 0\n",
    "            Trujet = 0 \n",
    "            \n",
    "        elif (airline=='Vistara'):\n",
    "            Jet_Airways = 0\n",
    "            IndiGo = 0\n",
    "            Air_India = 0\n",
    "            Multiple_carriers = 0\n",
    "            SpiceJet = 0\n",
    "            Vistara = 1\n",
    "            GoAir = 0\n",
    "            Multiple_carriers_Premium_economy = 0\n",
    "            Jet_Airways_Business = 0\n",
    "            Vistara_Premium_economy = 0\n",
    "            Trujet = 0\n",
    "\n",
    "        elif (airline=='GoAir'):\n",
    "            Jet_Airways = 0\n",
    "            IndiGo = 0\n",
    "            Air_India = 0\n",
    "            Multiple_carriers = 0\n",
    "            SpiceJet = 0\n",
    "            Vistara = 0\n",
    "            GoAir = 1\n",
    "            Multiple_carriers_Premium_economy = 0\n",
    "            Jet_Airways_Business = 0\n",
    "            Vistara_Premium_economy = 0\n",
    "            Trujet = 0\n",
    "\n",
    "        elif (airline=='Multiple carriers Premium economy'):\n",
    "            Jet_Airways = 0\n",
    "            IndiGo = 0\n",
    "            Air_India = 0\n",
    "            Multiple_carriers = 0\n",
    "            SpiceJet = 0\n",
    "            Vistara = 0\n",
    "            GoAir = 0\n",
    "            Multiple_carriers_Premium_economy = 1\n",
    "            Jet_Airways_Business = 0\n",
    "            Vistara_Premium_economy = 0\n",
    "            Trujet = 0\n",
    "\n",
    "        elif (airline=='Jet Airways Business'):\n",
    "            Jet_Airways = 0\n",
    "            IndiGo = 0\n",
    "            Air_India = 0\n",
    "            Multiple_carriers = 0\n",
    "            SpiceJet = 0\n",
    "            Vistara = 0\n",
    "            GoAir = 0\n",
    "            Multiple_carriers_Premium_economy = 0\n",
    "            Jet_Airways_Business = 1\n",
    "            Vistara_Premium_economy = 0\n",
    "            Trujet = 0\n",
    "\n",
    "        elif (airline=='Vistara Premium economy'):\n",
    "            Jet_Airways = 0\n",
    "            IndiGo = 0\n",
    "            Air_India = 0\n",
    "            Multiple_carriers = 0\n",
    "            SpiceJet = 0\n",
    "            Vistara = 0\n",
    "            GoAir = 0\n",
    "            Multiple_carriers_Premium_economy = 0\n",
    "            Jet_Airways_Business = 0\n",
    "            Vistara_Premium_economy = 1\n",
    "            Trujet = 0\n",
    "            \n",
    "        elif (airline=='Trujet'):\n",
    "            Jet_Airways = 0\n",
    "            IndiGo = 0\n",
    "            Air_India = 0\n",
    "            Multiple_carriers = 0\n",
    "            SpiceJet = 0\n",
    "            Vistara = 0\n",
    "            GoAir = 0\n",
    "            Multiple_carriers_Premium_economy = 0\n",
    "            Jet_Airways_Business = 0\n",
    "            Vistara_Premium_economy = 0\n",
    "            Trujet = 1\n",
    "\n",
    "        else:\n",
    "            Jet_Airways = 0\n",
    "            IndiGo = 0\n",
    "            Air_India = 0\n",
    "            Multiple_carriers = 0\n",
    "            SpiceJet = 0\n",
    "            Vistara = 0\n",
    "            GoAir = 0\n",
    "            Multiple_carriers_Premium_economy = 0\n",
    "            Jet_Airways_Business = 0\n",
    "            Vistara_Premium_economy = 0\n",
    "            Trujet = 0\n",
    "\n",
    "        # print(Jet_Airways,\n",
    "        #     IndiGo,\n",
    "        #     Air_India,\n",
    "        #     Multiple_carriers,\n",
    "        #     SpiceJet,\n",
    "        #     Vistara,\n",
    "        #     GoAir,\n",
    "        #     Multiple_carriers_Premium_economy,\n",
    "        #     Jet_Airways_Business,\n",
    "        #     Vistara_Premium_economy,\n",
    "        #     Trujet)\n",
    "\n",
    "        # Source\n",
    "        # Banglore = 0 (not in column)\n",
    "        Source = request.form[\"Source\"]\n",
    "        if (Source == 'Delhi'):\n",
    "            s_Delhi = 1\n",
    "            s_Kolkata = 0\n",
    "            s_Mumbai = 0\n",
    "            s_Chennai = 0\n",
    "\n",
    "        elif (Source == 'Kolkata'):\n",
    "            s_Delhi = 0\n",
    "            s_Kolkata = 1\n",
    "            s_Mumbai = 0\n",
    "            s_Chennai = 0\n",
    "\n",
    "        elif (Source == 'Mumbai'):\n",
    "            s_Delhi = 0\n",
    "            s_Kolkata = 0\n",
    "            s_Mumbai = 1\n",
    "            s_Chennai = 0\n",
    "\n",
    "        elif (Source == 'Chennai'):\n",
    "            s_Delhi = 0\n",
    "            s_Kolkata = 0\n",
    "            s_Mumbai = 0\n",
    "            s_Chennai = 1\n",
    "\n",
    "        else:\n",
    "            s_Delhi = 0\n",
    "            s_Kolkata = 0\n",
    "            s_Mumbai = 0\n",
    "            s_Chennai = 0\n",
    "\n",
    "        # print(s_Delhi,\n",
    "        #     s_Kolkata,\n",
    "        #     s_Mumbai,\n",
    "        #     s_Chennai)\n",
    "\n",
    "        # Destination\n",
    "        # Banglore = 0 (not in column)\n",
    "        Source = request.form[\"Destination\"]\n",
    "        if (Source == 'Cochin'):\n",
    "            d_Cochin = 1\n",
    "            d_Delhi = 0\n",
    "            d_New_Delhi = 0\n",
    "            d_Hyderabad = 0\n",
    "            d_Kolkata = 0\n",
    "        \n",
    "        elif (Source == 'Delhi'):\n",
    "            d_Cochin = 0\n",
    "            d_Delhi = 1\n",
    "            d_New_Delhi = 0\n",
    "            d_Hyderabad = 0\n",
    "            d_Kolkata = 0\n",
    "\n",
    "        elif (Source == 'New_Delhi'):\n",
    "            d_Cochin = 0\n",
    "            d_Delhi = 0\n",
    "            d_New_Delhi = 1\n",
    "            d_Hyderabad = 0\n",
    "            d_Kolkata = 0\n",
    "\n",
    "        elif (Source == 'Hyderabad'):\n",
    "            d_Cochin = 0\n",
    "            d_Delhi = 0\n",
    "            d_New_Delhi = 0\n",
    "            d_Hyderabad = 1\n",
    "            d_Kolkata = 0\n",
    "\n",
    "        elif (Source == 'Kolkata'):\n",
    "            d_Cochin = 0\n",
    "            d_Delhi = 0\n",
    "            d_New_Delhi = 0\n",
    "            d_Hyderabad = 0\n",
    "            d_Kolkata = 1\n",
    "\n",
    "        else:\n",
    "            d_Cochin = 0\n",
    "            d_Delhi = 0\n",
    "            d_New_Delhi = 0\n",
    "            d_Hyderabad = 0\n",
    "            d_Kolkata = 0\n",
    "\n",
    "        # print(\n",
    "        #     d_Cochin,\n",
    "        #     d_Delhi,\n",
    "        #     d_New_Delhi,\n",
    "        #     d_Hyderabad,\n",
    "        #     d_Kolkata\n",
    "        # )\n",
    "        \n",
    "\n",
    "    #     ['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour',\n",
    "    #    'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',\n",
    "    #    'Duration_mins', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',\n",
    "    #    'Airline_Jet Airways', 'Airline_Jet Airways Business',\n",
    "    #    'Airline_Multiple carriers',\n",
    "    #    'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',\n",
    "    #    'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',\n",
    "    #    'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',\n",
    "    #    'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',\n",
    "    #    'Destination_Kolkata', 'Destination_New Delhi']\n",
    "        \n",
    "        prediction=model.predict([[\n",
    "            Total_stops,\n",
    "            Journey_day,\n",
    "            Journey_month,\n",
    "            Dep_hour,\n",
    "            Dep_min,\n",
    "            Arrival_hour,\n",
    "            Arrival_min,\n",
    "            dur_hour,\n",
    "            dur_min,\n",
    "            Air_India,\n",
    "            GoAir,\n",
    "            IndiGo,\n",
    "            Jet_Airways,\n",
    "            Jet_Airways_Business,\n",
    "            Multiple_carriers,\n",
    "            Multiple_carriers_Premium_economy,\n",
    "            SpiceJet,\n",
    "            Trujet,\n",
    "            Vistara,\n",
    "            Vistara_Premium_economy,\n",
    "            s_Chennai,\n",
    "            s_Delhi,\n",
    "            s_Kolkata,\n",
    "            s_Mumbai,\n",
    "            d_Cochin,\n",
    "            d_Delhi,\n",
    "            d_Hyderabad,\n",
    "            d_Kolkata,\n",
    "            d_New_Delhi\n",
    "        ]])\n",
    "\n",
    "        output=round(prediction[0],2)\n",
    "\n",
    "        return render_template('home.html',prediction_text=\"Your Flight price is Rs. {}\".format(output))\n",
    "\n",
    "\n",
    "    return render_template(\"home.html\")\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
