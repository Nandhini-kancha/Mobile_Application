# Women Safety Application (Full-Stack Platform)

A comprehensive, dual-tier personal security platform featuring a native Android mobile application and a Python Flask REST API backend connected to a MongoDB database. The system provides active background monitoring, voice-activated emergency distress triggers, and predictive safety routing driven by machine learning.

---

## 🌟 Key Features

### 📱 Native Android App (Client)
* **Background Foreground Service**: Persistent, system-managed background listener that runs with low-priority notification status to bypass Android OS background throttling.
* **Continuous Voice SOS Activation**: Integrates native Android `SpeechRecognizer` to constantly parse microphone input. Instantly triggers emergency protocols if keywords (e.g., `"help"`, `"sos"`) are heard.
* **Offline SMS Fallback Broadcasting**: Uses the cellular network to broadcast real-time GPS location coordinates directly to emergency contacts when mobile internet is unavailable.
* **Predictive Routing & Maps Integration**: Uses Google Maps and Geocoding APIs to translate locations, query route safety parameters from the server, and draw color-coded safety polylines (Green = Safe road, Red = Risky shortcuts).
* **Hardware Step Tracker**: Communicates directly with the device's hardware pedometer (`Sensor.TYPE_STEP_DETECTOR`) to count walking statistics with negligible battery consumption.

### 🐍 Flask REST API (Backend)
* **User Management**: Simple endpoints to register users and maintain emergency contact configurations.
* **Active SOS Logs**: Real-time event logger that registers coordinates during active distress signals.
* **Safe Route Analyzer**: Receives route options and applies a machine learning model to evaluate the safety level of different pathways.
* **Keyword AI Parser**: A lightweight keyword classifier API to verify emergency phrases.

### 🤖 Machine Learning Core
* **Random Forest Classifier**: Features a `scikit-learn` predictive model trained on municipal environmental metrics:
  * `hour` (temporal risk)
  * `lighting` (ambient safety)
  * `crowd` (population density)
  * `police` (law enforcement presence)
  * `incidents` (historical risk indices)
* Generates route hazard coefficients to suggest the safest travel path.

---

## 🛠️ Technology Stack

* **Frontend**: Native Android (Java SDK 26+), Google Play Services (Location & Maps), Retrofit 3.0 (REST Client), Gson (JSON Serializer).
* **Backend**: Python 3.13+, Flask, MongoDB (PyMongo), scikit-learn (Random Forest).
* **Database**: MongoDB (NoSQL Document Store).

---

## 🚀 Setup & Installation

### 1. Backend Server Setup
1. Navigate to the `backend` directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Train and serialize the machine learning model:
   ```bash
   python train_safety_model.py
   ```
4. Run the development server:
   ```bash
   python app.py
   ```
   *(By default, the server will start on `http://localhost:5000`)*

### 2. Frontend Android Setup
1. Import the `frontend/app` folder into **Android Studio**.
2. Set up your Google Maps API Key:
   * Open `app/src/main/AndroidManifest.xml`.
   * Replace `YOUR_GOOGLE_MAPS_API_KEY` on line 53 with your custom Google Maps API key.
3. Configure the backend API address:
   * Open `app/src/main/java/com/example/womensafety/network/ApiClient.java`.
   * Update `BASE_URL` to point to your computer's local Wi-Fi IP address (e.g., `http://192.168.1.50:5000/api/`) so your testing phone/emulator can reach the server.
4. Sync Gradle and run the app on your device.

---

## 📂 Codebase Directory Structure

```text
├── backend/
│   ├── app.py                      # Flask REST endpoints
│   ├── database.py                 # MongoDB configuration
│   ├── ai_engine.py                # Keyword text classifier
│   ├── train_safety_model.py       # ML Random Forest training script
│   └── requirements.txt            # Python dependencies
└── frontend/app/
    ├── src/main/AndroidManifest.xml# Android permissions and services config
    └── src/main/java/com/example/womensafety/
        ├── MainActivity.java       # User dashboard and SOS control hub
        ├── SafeRouteActivity.java  # Google Maps path safety visualizer
        ├── RegisterActivity.java   # Profile registration
        ├── GuardiansActivity.java  # Contacts list (RecyclerView)
        └── services/
            └── SafetyForegroundService.java # Speech recognizer & pedometer listener
```

---

## 🔒 Security & Privacy Notice
* The Speech Recognizer runs fully locally on the Android device to protect voice privacy.
* All network transmissions should be secured using HTTPS (TLS) in production environments.
* Keep the Google Maps API Key restricted via Google Cloud Console to prevent unauthorized usage.
