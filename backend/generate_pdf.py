import os
import sys
from fpdf import FPDF

class InterviewPrepPDF(FPDF):
    def header(self):
        # Skip header on the cover page (Page 1)
        if self.page_no() == 1:
            return
        
        # Header styling
        self.set_fill_color(26, 54, 93)  # Navy Blue #1A365D
        self.rect(0, 0, 210, 15, 'F')
        
        self.set_y(4)
        self.set_text_color(255, 255, 255)
        self.set_font('Helvetica', 'B', 9)
        self.cell(0, 7, 'WOMEN SAFETY APP - TECHNICAL DOSSIER & INTERVIEW STUDY GUIDE', align='C', ln=True)
        
        # Top margin spacing below header
        self.set_y(22)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(115, 115, 115)  # Medium grey
        
        # Rule line above footer
        self.set_draw_color(226, 232, 240)  # light border
        self.line(15, self.get_y(), 195, self.get_y())
        
        self.cell(0, 10, f'Confidential - Interview Preparation Document  |  Page {self.page_no()} of {{nb}}', align='C')

    def add_heading(self, text, level=1):
        if level == 1:
            self.set_font('Helvetica', 'B', 16)
            self.set_text_color(26, 54, 93)  # Navy
            self.ln(6)
            self.cell(0, 8, text, ln=True)
            self.set_draw_color(43, 108, 176)  # Secondary Blue #2B6CB0
            self.set_line_width(0.8)
            self.line(self.get_x(), self.get_y() + 1, self.get_x() + 45, self.get_y() + 1)
            self.ln(4)
        elif level == 2:
            self.set_font('Helvetica', 'B', 12)
            self.set_text_color(43, 108, 176)  # Secondary Blue
            self.ln(4)
            self.cell(0, 6, text, ln=True)
            self.ln(2)
        elif level == 3:
            self.set_font('Helvetica', 'B', 10)
            self.set_text_color(74, 85, 104)  # Charcoal
            self.ln(3)
            self.cell(0, 5, text, ln=True)
            self.ln(1)

    def add_paragraph(self, text):
        self.set_font('Helvetica', '', 9.5)
        self.set_text_color(45, 55, 72)  # Charcoal
        self.multi_cell(0, 5, text)
        self.ln(2)

    def add_bullet(self, title, text):
        self.set_font('Helvetica', 'B', 9.5)
        self.set_text_color(43, 108, 176)
        self.write(5, "  *  " + title + ": ")
        self.set_font('Helvetica', '', 9.5)
        self.set_text_color(45, 55, 72)
        self.multi_cell(0, 5, text)
        self.ln(1)

    def add_q_and_a(self, question, answer):
        # Draw a light grey box for interview Q&As
        self.set_fill_color(247, 250, 252) # ultra light grey #F7FAFC
        self.set_draw_color(226, 232, 240) # light border #E2E8F0
        self.set_line_width(0.3)
        
        # Create a temp variable to check vertical space
        # Height prediction: question lines + answer lines
        q_len = len(question)
        a_len = len(answer)
        est_lines = (q_len / 75) + (a_len / 75) + 3
        est_height = est_lines * 5
        
        # Page break if near bottom
        if (self.get_y() + est_height) > 270:
            self.add_page()
            
        start_y = self.get_y()
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(26, 54, 93)
        self.multi_cell(0, 5.5, "Q: " + question, border=0, fill=True)
        self.ln(1)
        
        self.set_font('Helvetica', '', 9.5)
        self.set_text_color(45, 55, 72)
        self.multi_cell(0, 5, "A: " + answer, border=0, fill=True)
        end_y = self.get_y()
        
        # Draw left border line as a visual accent
        self.set_draw_color(43, 108, 176) # blue vertical bar
        self.set_line_width(1.5)
        self.line(self.get_x(), start_y, self.get_x(), end_y)
        self.ln(4)

def build_pdf():
    pdf = InterviewPrepPDF(orientation='P', unit='mm', format='A4')
    pdf.alias_nb_pages()
    pdf.set_margins(15, 20, 15)
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # ------------------ PAGE 1: COVER PAGE ------------------
    pdf.add_page()
    
    # Vertical styling bar on left
    pdf.set_fill_color(26, 54, 93)
    pdf.rect(0, 0, 10, 297, 'F')
    
    pdf.set_x(25)
    pdf.ln(40)
    
    # Title
    pdf.set_font('Helvetica', 'B', 28)
    pdf.set_text_color(26, 54, 93)
    pdf.cell(0, 12, 'WOMEN SAFETY APP', ln=True)
    
    # Subtitle
    pdf.set_font('Helvetica', 'B', 14)
    pdf.set_text_color(43, 108, 176)
    pdf.cell(0, 10, 'Full-Stack Technical Analysis & Complete Interview Guide', ln=True)
    
    # Divider line
    pdf.ln(5)
    pdf.set_draw_color(43, 108, 176)
    pdf.set_line_width(1.5)
    pdf.line(25, pdf.get_y(), 105, pdf.get_y())
    pdf.ln(15)
    
    # Overview Summary
    pdf.set_x(25)
    pdf.set_font('Helvetica', '', 10.5)
    pdf.set_text_color(74, 85, 104)
    desc_text = (
        "An in-depth systems analysis of the Women Safety Platform, detailed for "
        "architectural walkthroughs and system-design assessments in professional interviews. "
        "Covers Android Client architecture, Flask REST Backend interfaces, MongoDB schema structure, "
        "and Random Forest Predictive Machine Learning models."
    )
    pdf.multi_cell(0, 6, desc_text)
    
    pdf.ln(60)
    
    # Info Panel
    pdf.set_x(25)
    pdf.set_fill_color(247, 250, 252)
    pdf.set_draw_color(226, 232, 240)
    pdf.set_line_width(0.5)
    
    # Draw info box
    box_start_y = pdf.get_y()
    pdf.multi_cell(0, 7, "", border=1, fill=True)
    box_end_y = pdf.get_y()
    
    # Put text inside
    pdf.set_y(box_start_y + 3)
    pdf.set_x(28)
    pdf.set_font('Helvetica', 'B', 9.5)
    pdf.set_text_color(26, 54, 93)
    pdf.write(5, "Platform: ")
    pdf.set_font('Helvetica', '', 9.5)
    pdf.set_text_color(45, 55, 72)
    pdf.cell(0, 5, "Android Native (Java SDK 26+) & Python Flask REST Backend", ln=True)
    
    pdf.set_x(28)
    pdf.set_font('Helvetica', 'B', 9.5)
    pdf.set_text_color(26, 54, 93)
    pdf.write(5, "Database: ")
    pdf.set_font('Helvetica', '', 9.5)
    pdf.set_text_color(45, 55, 72)
    pdf.cell(0, 5, "MongoDB (NoSQL Document Store)", ln=True)
    
    pdf.set_x(28)
    pdf.set_font('Helvetica', 'B', 9.5)
    pdf.set_text_color(26, 54, 93)
    pdf.write(5, "AI/ML Core: ")
    pdf.set_font('Helvetica', '', 9.5)
    pdf.set_text_color(45, 55, 72)
    pdf.cell(0, 5, "Random Forest Classifier (Predictive Safe Routing)", ln=True)
    
    pdf.set_x(28)
    pdf.set_font('Helvetica', 'B', 9.5)
    pdf.set_text_color(26, 54, 93)
    pdf.write(5, "Target Roles: ")
    pdf.set_font('Helvetica', '', 9.5)
    pdf.set_text_color(45, 55, 72)
    pdf.cell(0, 5, "Android Engineer / Full-Stack Engineer / Python Backend Developer", ln=True)
    
    # ------------------ PAGE 2: SYSTEM ARCHITECTURE & OVERVIEW ------------------
    pdf.add_page()
    pdf.add_heading("1. Executive Summary & Core Value Proposition")
    pdf.add_paragraph(
        "The Women Safety Platform is a dual-tier client-server application built to offer immediate protection "
        "and proactive risk prevention. Unlike static distress apps that only support manual buttons, this platform "
        "features real-time background protection, speech pattern analyzing systems, predictive safe routing, and "
        "hardware step metrics."
    )
    
    pdf.add_heading("2. System Architecture & Component Mapping", level=2)
    pdf.add_paragraph(
        "The platform utilizes an asynchronous client-server model to ensure the client remains active and lightweight "
        "while offloading heavy database processing and predictive modeling to the remote server:"
    )
    
    pdf.add_bullet("Native Android Application", "Responsible for local device states, including step counters, microphone streams, continuous speech processing, offline SMS broadcasting, and displaying safe routing maps using the Google Maps SDK.")
    pdf.add_bullet("Python Flask Web Server", "Exposes REST endpoints to register user instances, receive background distress triggers, accept live coordinates updates, and execute safety predictive classifiers.")
    pdf.add_bullet("MongoDB Database", "Stores persistent user registrations, contact associations, active alerts logs, and tracking history.")
    pdf.add_bullet("Random Forest Safety Model", "Evaluates travel routing paths based on environmental attributes (time, crowd density, police patrol presence, light indexes, and incident logs).")
    
    pdf.add_heading("3. Component Interaction Flowchart", level=2)
    pdf.add_paragraph(
        "1. Client registers/updates details -> POST to Flask -> Saved in MongoDB.\n"
        "2. Foreground Service runs in background -> listents for voice keywords / triggers step counter.\n"
        "3. Voice SOS triggered -> Sends SMS to Emergency Contacts + POST /api/alert/trigger -> Saved in MongoDB.\n"
        "4. Safe Route Request -> Geocodes address on client -> POST /api/route/analyze -> Flask executes Random Forest model -> Returns route polylines -> Client colors paths (Green=Safe, Red=Risky)."
    )

    # ------------------ PAGE 3: FRONTEND AND SERVICE ARCHITECTURE ------------------
    pdf.add_page()
    pdf.add_heading("2. Frontend Mobile Client Architecture")
    pdf.add_paragraph(
        "The frontend is implemented as a native Android application using Java, structured around Activities "
        "for UI and a persistent Foreground Service for backend protection. This allows the application to stay active "
        "even when minimized or when the screen is locked."
    )
    
    pdf.add_heading("Android Core Activities Breakdown", level=2)
    
    pdf.add_bullet("MainActivity.java", "Serves as the dashboard. Checks and requests runtime permissions. Manages the lifecycle of the SafetyForegroundService. Implements a large manual SOS button which immediately fetches coordinates from the FusedLocationProviderClient, broadcasts distress messages to guardians via SmsManager, and registers the alert with the remote server via Retrofit.")
    pdf.add_bullet("SafeRouteActivity.java", "Integrates Google Maps API. Translates human-readable start/destination text queries into spatial coordinates via Geocoder. Retrofit requests /api/route/analyze to retrieve multiple route options. Draws polylines with safety score coding: green for scores > 0.70 (safe road), red for lower scores (unsafe shortcuts).")
    pdf.add_bullet("RegisterActivity.java", "Handles user profile creation. Captures names, cell phone numbers, and emergency contacts. Communicates with /api/register to get a global user ID and persists the configuration locally using SharedPreferences.")
    pdf.add_bullet("GuardiansActivity.java", "Manages the emergency contacts list. Displays values in a RecyclerView list. Operations (addition/deletion) synchronize instantly to local SharedPreferences storage.")
    
    pdf.add_heading("Background Service & Sensor Listeners", level=2)
    pdf.add_bullet("SafetyForegroundService.java", "Starts as a sticky service (START_STICKY) running a visible persistent status notification to prevent OS-level termination. Integrates continuous voice listening using Android native SpeechRecognizer. It runs step detection sensors to record walking progress.")
    pdf.add_bullet("SpeechRecognizer Lifecycle", "Continuous speech analysis runs in the background. On hearing 'help' or 'sos', the speech recognizer activates the emergency protocol. To handle microphone drop-outs, the onError() callback automatically restarts the voice recognition engine.")
    pdf.add_bullet("Hardware Sensor Integration", "Implements SensorEventListener utilizing Sensor.TYPE_STEP_DETECTOR. Tracks walking steps, calculates distance based on average human step index (0.762m), and broadcasts step updates locally.")

    # ------------------ PAGE 4: BACKEND AND AI CORE ------------------
    pdf.add_page()
    pdf.add_heading("3. Backend & AI Predictive Engine")
    pdf.add_paragraph(
        "The backend is a Flask web service serving REST APIs. It handles user state registration, location tracking updates, "
        "and executes predictive machine learning models to classify routes and evaluate emergency keywords."
    )
    
    pdf.add_heading("API Route Specifications", level=2)
    
    pdf.add_bullet("GET /", "Health check API to verify database and server online status.")
    pdf.add_bullet("POST /api/register", "Registers a new user record. Parameters: 'name', 'phone', 'contacts' (list). Persists record in MongoDB and returns unique user_id.")
    pdf.add_bullet("POST /api/alert/trigger", "Registers active SOS events with starting coordinate values (lat, lng). Generates log records in MongoDB.")
    pdf.add_bullet("POST /api/alert/location", "Updates GPS coordinates of active emergency instances. Tracks live device movement.")
    pdf.add_bullet("POST /api/route/analyze", "Performs route risk analysis. Uses the machine learning model to evaluate waypoints based on current time, lighting levels, crowd levels, police presence, and historical incidents.")
    pdf.add_bullet("POST /api/ai/analyze", "Receives speech-to-text text strings. Parses against emergency critical keywords, returning emergency status (True/False).")
    
    pdf.add_heading("Database Collection Schemas (MongoDB)", level=2)
    pdf.add_bullet("users collection", "Stores: name (String), phone (String), contacts (Array of Strings), created_at (DateTime). Indexed by phone number for quick lookups.")
    pdf.add_bullet("alerts collection", "Stores: user_id (String), latitude (Double), longitude (Double), timestamp (DateTime), status (String - active/resolved), last_updated (DateTime).")
    
    pdf.add_heading("AI & Machine Learning Core", level=2)
    pdf.add_bullet("Random Forest Model", "Trained on synthetic municipal environmental data. Takes 5 inputs: hour (0-23), lighting (0-2), crowd (0-2), police (0-1), incidents (0-1). Predicts safety (0 = Unsafe, 1 = Safe). RandomForestClassifier uses 100 trees for robust decision splits.")
    pdf.add_bullet("Safety Score Formula", "Scores are computed dynamically. Flask combines model binary classification with random variations to return scores (e.g. 0.85-0.97 for safe paths, 0.25-0.40 for unsafe paths) and detailed safety explanations.")
    pdf.add_bullet("Emergency Text Parser", "EmergencyClassifier inside ai_engine.py implements keyword checks. It parses input strings for words like 'help', 'save me', 'police', 'danger', 'sos', 'attack', 'following me', 'knife', 'emergency' for rapid emergency detection.")

    # ------------------ PAGE 5: INTERVIEW Q&A - ANDROID ------------------
    pdf.add_page()
    pdf.add_heading("4. Interview Preparation: Q&A Guide")
    pdf.add_paragraph(
        "This section covers technical interview questions regarding the system, architecture, and framework APIs, "
        "divided by domains (Android, Backend, ML, System Design)."
    )
    
    pdf.add_heading("Android Framework & Application Logic", level=2)
    
    pdf.add_q_and_a(
        "Why is a Foreground Service used instead of a standard Background Service?",
        "Android restricts background execution (limits start in Android 8.0, reinforced in Android 14+). Standard services are killed minutes after the app is minimized. A Foreground Service displays a persistent notification, showing it is active. Since Android 14, we must explicitly declare foregroundServiceType ('location|microphone' in our manifest) to access location and microphone in the background. Without it, the OS throws a SecurityException."
    )
    
    pdf.add_q_and_a(
        "How do you handle runtime permissions in Android, and what permissions are requested?",
        "Permissions requested are ACCESS_FINE_LOCATION (accurate location), RECORD_AUDIO (speech recognition), SEND_SMS (guardian alerts), CALL_PHONE (helplines), and POST_NOTIFICATIONS (required in Android 13+ to show foreground service notifications). The app checks state using ContextCompat.checkSelfPermission. If missing, it requests them via ActivityCompat.requestPermissions and handles responses in onRequestPermissionsResult. For background tracking, ACCESS_BACKGROUND_LOCATION is also requested."
    )
    
    pdf.add_q_and_a(
        "How is the SpeechRecognizer kept running continuously? What happens if there's an error?",
        "In SafetyForegroundService, after setting up the SpeechRecognizer, we implement a RecognitionListener. In both the onResults() and onError() callbacks, we call speechRecognizer.startListening(recognizerIntent) again. This creates a loop that restarts listening. For example, if a network timeout or speech timeout occurs (triggering onError), the engine restarts immediately instead of crashing or stopping."
    )
    
    pdf.add_q_and_a(
        "How does the step counter work without draining battery?",
        "We utilize Sensor.TYPE_STEP_DETECTOR. Unlike Sensor.TYPE_ACCELEROMETER, which requires continuous CPU math to calculate steps, the hardware step detector is an onboard sensor that triggers an event on each step. The CPU remains asleep until a step is detected, making it power-efficient."
    )

    # ------------------ PAGE 6: INTERVIEW Q&A - BACKEND & ML ------------------
    pdf.add_page()
    pdf.add_heading("Backend, Database & Machine Learning Q&A", level=2)
    
    pdf.add_q_and_a(
        "Why is MongoDB chosen for the database layer?",
        "1. Flexible Schema: Emergency contact structures, route logs, and location coordinates change. A document store (JSON-like documents) fits this easily. 2. Geographic Querying: MongoDB has native support for GeoJSON indices (2dsphere). In a production environment, this allows us to run spatial queries (like finding active alerts within 1km or finding nearby police stations) with low latency. 3. High Write Throughput: Location updates generate write streams. MongoDB scales writes horizontally."
    )
    
    pdf.add_q_and_a(
        "Why use a Random Forest model for safety route analysis, and how does it make predictions?",
        "A Random Forest is an ensemble classifier that builds multiple decision trees and merges their results for stability. We feed it 5 key inputs: hour, lighting index, crowd density, police proximity, and past incident history. It is highly interpretable, runs quickly, and prevents overfitting compared to deep learning models. In a production scenario, we can convert it to ONNX or TensorFlow Lite to run directly on the mobile client, making predictions work offline."
    )
    
    pdf.add_q_and_a(
        "How do you secure communications between the mobile application and the REST server?",
        "1. Transport Security: Enforce HTTPS (TLS 1.3) to encrypt payloads, avoiding man-in-the-middle attacks. 2. Device Auth: Implement JWT (JSON Web Tokens). When a user registers, the server generates a token. The client stores it in SharedPreferences and attaches it to the 'Authorization: Bearer <token>' header for subsequent requests. 3. Request Validation: Validate coordinates, filter SQL/NoSQL injection, and rate-limit routes using Flask-Limiter."
    )
    
    pdf.add_q_and_a(
        "If a user is in an area with no internet, how does the application handle it?",
        "This app implements a hybrid offline-online strategy. Triggering the SOS button immediately broadcasts an SMS containing a Google Maps link to the emergency contacts using the cell network (offline). Concurrently, it sends a Retrofit network call to register the event on the web database. If the network call fails, the client uses an offline fallback, showing a Toast, while the SMS ensures the guardians are still notified."
    )

    # ------------------ PAGE 7: FOLLOW-UP QUESTIONS & SYSTEMS IMPROVEMENTS ------------------
    pdf.add_page()
    pdf.add_heading("5. Follow-Up Questions & Architectural Improvements")
    pdf.add_paragraph(
        "Interviewers often ask how you would improve or scale the current code. Use these structured points "
        "to show your system engineering capabilities."
    )
    
    pdf.add_heading("Likely Follow-up Questions in an Interview", level=2)
    
    pdf.add_bullet("Q1. How would you handle battery drain caused by continuous background location and audio listening?", 
                   "I would implement adaptive sampling. For location, use the Accelerometer to check if the user is stationary. If they aren't moving, reduce GPS updates from every 10 seconds to every 5 minutes. For audio, instead of keeping the speech recognizer active, I would use a low-power wake-word engine (like Porcupine or Snowboy) that runs locally on hardware DSP, and only spin up the full speech engine once the wake word 'SOS' is detected.")
    
    pdf.add_bullet("Q2. How do you scale the backend to support millions of active users sending location updates?", 
                   "I would introduce a message broker like Apache Kafka or RabbitMQ. When location updates (/api/alert/location) arrive, the Flask server logs them directly to a fast queue instead of writing directly to MongoDB. A worker service then reads from the queue and updates MongoDB in batches. I would also cache the active user profiles in Redis to avoid hitting MongoDB for every API authentication check.")
    
    pdf.add_bullet("Q3. The current NLP engine uses simple keyword matching. How would you handle more complex situations?", 
                   "The keyword classifier inside ai_engine.py is vulnerable to false positives (e.g. saying 'Can you help me find my keys?'). I would replace this with an intent classifier. For example, we could train a light DistilBERT model or run a local MobileBERT model on Android using ONNX. This classifier would analyze the sentence context and output an emergency probability, reducing false alarms.")
    
    pdf.add_bullet("Q4. How do you handle cases where the app is closed by the user or force-stopped by the operating system?", 
                   "In Android, if the user swipes away the app from the recents list, the service can survive if it is a Foreground Service. However, if the OS force-stops the app (due to aggressive battery optimization), all services are killed. To counter this, I would register a BroadcastReceiver that listens for system broadcasts like BOOT_COMPLETED or MY_PACKAGE_REPLACED to automatically restart the service. I would also guide the user to disable battery optimization in their device settings.")

    pdf.add_heading("Strategic Interview Presentation Tips", level=2)
    pdf.add_paragraph(
        "1. Highlight Android 14+ details: Mention how you declare and handle foregroundServiceType. This shows you are up-to-date with Android security policies.\n"
        "2. Explain the offline-first design: Focus on how sending the SMS is the primary, reliable fallback, and the web backend API is secondary. This shows you build resilient systems.\n"
        "3. Discuss model deployment: Explain that while the model is trained in Python, it can be exported as a TFLite file to run on Android. This demonstrates edge AI capabilities."
    )
    
    # Save the file
    pdf_filename = "Women_Safety_Project_Interview_Prep.pdf"
    pdf.output(pdf_filename)
    print(f"PDF generated successfully: {pdf_filename}")

if __name__ == "__main__":
    build_pdf()
