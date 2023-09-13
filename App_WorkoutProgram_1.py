from tkinter import Tk, Frame, Label, Checkbutton, BooleanVar, Button, W, E, Entry, StringVar, Toplevel, Message, OptionMenu, messagebox
from datetime import datetime


# Function to show exercise information
def show_info(exercise_info, how_to_info):
    top = Toplevel()
    top.geometry('300x200')
    msg = Message(top, text=f"Benefits: {exercise_info}\n\nHow To: {how_to_info}", width=280)
    msg.pack()


# Function to save workout program in HTML format
def save_workout_program():
    selected_exercises = {
        'Cardio': [],
        'Strength': [],
        'Flexibility': [],
        'Mental': []  # Added Mental category
    }
    user_provided_name = name_var.get()

    for exercise_name, input_data in exercise_inputs.items():
        if input_data['var'].get():
            exercise_info = {
                'name': exercise_name,
                'sets': input_data['sets_var'].get(),
                'reps': input_data['reps_var'].get(),
                'duration': input_data['duration_var'].get(),
                'weight': input_data['weight_var'].get()
            }

            for category in category_exercises.keys():
                if exercise_name in [exercise['name'] for exercise in category_exercises[category]]:
                    selected_exercises[category].append(exercise_info)

    now = datetime.now()
    formatted_time = now.strftime("%A %d.%m %Y")
    file_name = f"{user_provided_name}_{formatted_time}.html"

    with open(file_name, 'w') as file:
        file.write("<html><body>")
        file.write("<h1>Workout Planner</h1>")
        file.write("<hr>")
        file.write(f"<p>Generated on: {formatted_time}</p>")
        file.write(f"<p>Day of the Week: {day_var.get()}</p>")
        file.write("<hr>")
        file.write('<table style="width:100%">')

        for category, exercises in selected_exercises.items():
            if exercises:
                file.write('<td style="vertical-align:top">')
                file.write(f"<h2>{category} Exercises:</h2>")

                for exercise_info in exercises:
                    exercise_name = exercise_info["name"]
                    info = [exercise['info'] for exercise in category_exercises[category] if
                            exercise['name'] == exercise_name][0]
                    how_to = [exercise['how_to'] for exercise in category_exercises[category] if
                              exercise['name'] == exercise_name][0]

                    # Escape special characters
                    escaped_info = info.replace("'", "\\'").replace("\n", "\\n")
                    escaped_how_to = how_to.replace("'", "\\'").replace("\n", "\\n")

                    file.write(f'<input type="checkbox" id="{exercise_name}" name="{exercise_name}">')
                    file.write(f'<label for="{exercise_name}"><strong>Exercise:</strong> {exercise_name}</label><br>')
                    file.write(f"Sets: {exercise_info['sets']}<br>")
                    file.write(f"Reps: {exercise_info['reps']}<br>")
                    file.write(f"Duration (mins): {exercise_info['duration']}<br>")
                    file.write(f"Weight (KG): {exercise_info['weight']}<br>")
                    file.write(
                        f'<button onclick="alert(\'{escaped_info}\\n\\nHow to: {escaped_how_to}\')">Info</button><hr>')

                file.write('</td>')

        file.write('</table>')
        file.write("<hr>")
        file.write("</body></html>")

    response = messagebox.askyesno("Success", "Workout plan saved successfully as HTML. Would you like to continue?")
    if not response:
        root.quit()


def create_input_boxes(frame, row):
    duration_var = StringVar()
    sets_var = StringVar()
    reps_var = StringVar()
    weight_var = StringVar()

    Entry(frame, textvariable=sets_var, width=5).grid(row=row, column=2, padx=5, pady=2)
    Entry(frame, textvariable=reps_var, width=5).grid(row=row, column=4, padx=5, pady=2)
    Entry(frame, textvariable=duration_var, width=5).grid(row=row, column=6, padx=5, pady=2)
    Entry(frame, textvariable=weight_var, width=5).grid(row=row, column=8, padx=5, pady=2)

    return {'var': BooleanVar(), 'duration_var': duration_var, 'sets_var': sets_var, 'reps_var': reps_var, 'weight_var': weight_var}


# Create the main window
root = Tk()
root.title("WORKOUT PLANNER")
root.geometry('1200x800')

# Entry box for user to name their workout plan
name_var = StringVar()
Label(root, text="Workout Name:").grid(row=6, column=0, pady=10, sticky=E)
name_entry = Entry(root, textvariable=name_var)
name_entry.grid(row=6, column=1, pady=10)

# Initialize exercise inputs
exercise_inputs = {}

category_exercises = {
    'Cardio': [
        {'name': 'Jogging',
         'info': 'Jogging is a versatile cardiovascular exercise that significantly improves heart health, burns calories, and enhances overall endurance. It also strengthens leg muscles, contributing to a balanced lower body workout.',
         'how_to': 'To jog effectively, begin by running at a steady pace that allows you to maintain a comfortable rhythm. Keep your back straight and your arms gently swinging by your sides. Breathe consistently and enjoy the rhythmic motion of your run.'},

        {'name': 'Cycling',
         'info': 'Cycling offers a dual benefit by providing an excellent cardiovascular workout and targeting the leg muscles. It\'s particularly effective for enhancing cardiovascular endurance and toning the lower body.',
         'how_to': 'Ride a bike at a moderate to fast pace. Maintain a smooth pedaling motion and focus on maintaining proper posture throughout the ride. Adjust the resistance as needed to challenge yourself.'},

        {'name': 'Swimming',
         'info': 'Swimming is a full-body workout that offers outstanding cardiovascular benefits. It engages various muscle groups while promoting heart health and endurance.',
         'how_to': 'Swim laps in a pool, focusing on maintaining a consistent and rhythmic stroke. Alternate between different strokes to work different muscle groups and enjoy a comprehensive workout.'},

        {'name': 'Elliptical',
         'info': 'The elliptical machine provides a low-impact cardio workout that also engages the upper body. It\'s an effective way to improve cardiovascular health while giving your joints a break.',
         'how_to': 'Use an elliptical machine at a moderate pace. Hold onto the handles and use a fluid motion to move your legs back and forth. Push and pull the handles to engage your upper body as well.'},

        {'name': 'Rowing',
         'info': 'Rowing is a versatile exercise that combines cardiovascular conditioning with upper body and core strength training. It\'s an effective way to achieve a full-body workout.',
         'how_to': 'Use a rowing machine to simulate rowing on water. Push with your legs, engage your core, and pull the handles towards your chest. Maintain a fluid motion and control the resistance for a challenging workout.'},

        {'name': 'Jumping Jacks',
         'info': 'Jumping jacks offer a quick and effective cardiovascular workout that also improves coordination. This classic exercise engages multiple muscle groups and gets your heart pumping.',
         'how_to': 'Start by standing with your feet together and arms by your sides. Jump while simultaneously spreading your legs and raising your arms above your head. Return to the starting position with a second jump.'},

        {'name': 'Burpees',
         'info': 'Burpees are a high-intensity cardio exercise that targets multiple muscle groups while elevating your heart rate. They provide an efficient way to build strength and endurance.',
         'how_to': 'Begin from a standing position, drop into a squat, and kick your feet back into a plank. Perform a push-up, then reverse the motion: bring your feet back to the squat position and jump explosively.'},

        {'name': 'Stair Climbing',
         'info': 'Stair climbing is an effective cardio exercise that also strengthens the leg muscles. It offers a practical way to incorporate cardiovascular fitness into your daily routine.',
         'how_to': 'Find a set of stairs or use a stair climber machine. Climb up and down the stairs at a steady pace. Keep your posture upright and engage your leg muscles with each step.'},

        {'name': 'Sprinting',
         'info': 'Sprinting is a high-intensity running exercise that helps build speed and power. It engages the cardiovascular system while targeting fast-twitch muscle fibers.',
         'how_to': 'Run as fast as possible for short distances. Focus on powerful strides and pumping your arms. Allow adequate rest between sprints to maintain intensity.'},

        {'name': 'Walking',
         'info': 'Walking is a low-impact cardiovascular exercise that\'s gentle on the joints. It\'s an accessible way to improve heart health and maintain overall fitness.',
         'how_to': 'Walk at a brisk pace, swinging your arms as you go. Maintain proper posture and focus on taking consistent steps.'},

        {'name': 'High Knees',
         'info': 'High knees offer a dynamic cardio workout that also engages the leg muscles. This exercise enhances coordination and provides an effective way to elevate your heart rate.',
         'how_to': 'Stand up straight and start jogging in place, bringing your knees as high as possible with each step. Pump your arms to match the rhythm of your knees.'},

        {'name': 'Mountain Climbers',
         'info': 'Mountain climbers are a versatile cardio exercise that targets the core and leg muscles. They also elevate your heart rate, making them great for cardiovascular conditioning.',
         'how_to': 'Start in a plank position with your hands directly under your shoulders. Alternate drawing your knees towards your chest, engaging your core and maintaining a quick pace.'},

        {'name': 'Boxing',
         'info': 'Boxing is a cardiovascular exercise that improves heart health while enhancing upper body strength. It offers a full-body workout and is a fun way to challenge yourself.',
         'how_to': 'Adopt a boxing stance and throw punches with proper form. Engage your core and use your entire body to generate power with each punch. Incorporate footwork to simulate a real boxing match.'},

        {'name': 'Jump Rope',
         'info': 'Jump rope is an effective and versatile cardio exercise that also enhances coordination. It\'s an excellent way to burn calories and improve cardiovascular fitness.',
         'how_to': 'Hold the handles of a jump rope and swing it over your head. Jump over the rope as it approaches your feet. Keep a steady rhythm and gradually increase your speed.'},

        {'name': 'Skating',
         'info': 'Skating provides a low-impact cardio workout that\'s gentle on the joints. It engages various muscle groups and offers an enjoyable way to elevate your heart rate.',
         'how_to': 'Glide on skates or a skateboard, pushing off with one foot at a time. Maintain balance and use your arms to help control your movement.'},

        {'name': 'Zumba',
         'info': 'Zumba is a dance-based cardio workout that combines fitness with fun. It\'s an energetic way to improve cardiovascular health while enjoying music and movement.',
         'how_to': 'Follow a series of dance moves set to music. Allow yourself to let loose and enjoy the rhythm while getting an effective cardio workout.'},

        {'name': 'Tai Chi',
         'info': 'Tai Chi is a gentle and low-impact exercise that promotes relaxation and balance. It involves slow, deliberate movements and deep breathing.',
         'how_to': 'Perform a series of postures in a slow, focused manner. Coordinate your movements with your breath, allowing a sense of tranquility to accompany your exercise.'},

        {'name': 'Kickboxing',
         'info': 'Kickboxing combines elements of boxing and martial arts to provide a dynamic cardio workout. It engages the entire body while enhancing cardiovascular fitness.',
         'how_to': 'Execute a series of kicks and punches, maintaining proper form and balance. Coordinate your movements to the rhythm of your chosen music for an energetic workout.'},

        {'name': 'Treadmill',
         'info': 'The treadmill offers a convenient way to engage in walking or running exercises indoors. It\'s a versatile cardio machine that allows you to control the intensity of your workout.',
         'how_to': 'Walk or run on the treadmill, adjusting the speed and incline to match your fitness level. Hold onto the handles for stability, and maintain a natural stride.'},

        {'name': 'Crossfit',
         'info': 'CrossFit workouts involve high-intensity exercises that vary from day to day. They offer a diverse and challenging way to improve cardiovascular fitness and overall strength.',
         'how_to': 'Follow the Workout of the Day (WOD) at a CrossFit gym. Engage in a combination of functional movements that target different muscle groups and elevate your heart rate.'},

        {'name': 'HIIT',
         'info': 'High-Intensity Interval Training (HIIT) involves short bursts of intense exercise followed by rest or low-intensity periods. It\'s an efficient way to burn calories and improve cardiovascular health.',
         'how_to': 'Perform high-intensity exercises like sprinting or burpees for short durations, followed by a rest period. Repeat the cycle for several rounds to maximize the benefits.'},

        {'name': 'Hiking',
         'info': 'Hiking provides a cardio workout with the added benefit of being immersed in nature. It engages the leg muscles and promotes cardiovascular health while offering a refreshing experience.',
         'how_to': 'Explore trails or uneven terrain by walking at a brisk pace. Engage your leg muscles and enjoy the natural surroundings as you elevate your heart rate.'},

        {'name': 'Skiing',
         'info': 'Skiing is a seasonal outdoor activity that offers a great cardiovascular workout. It engages various muscle groups and provides an exhilarating way to enjoy the winter months.',
         'how_to': 'Glide down snowy slopes on skis, using your leg muscles to steer and control your speed. Maintain balance and enjoy the thrill of skiing.'},

        {'name': 'Paddleboarding',
         'info': 'Paddleboarding provides a unique way to improve balance while engaging in a moderate cardio workout. It targets various muscle groups and allows you to explore bodies of water.',
         'how_to': 'Stand on a board in a body of water and use a paddle to propel yourself forward. Engage your core and leg muscles to maintain balance as you paddle.'},

        {'name': 'Dancing',
         'info': 'Dancing is a fun and engaging way to improve cardiovascular health. It offers a full-body workout while allowing you to express yourself through movement and music.',
         'how_to': 'Move to music in a rhythmic manner, allowing your body to flow with the beat. Experiment with different dance styles to challenge yourself and keep the workout exciting.'},
],

    'Strength': [
        {'name': 'Push-Ups',
         'info': 'Push-ups are a classic bodyweight exercise that effectively target the chest, shoulders, and triceps. They help build upper body strength and stability.',
         'how_to': 'Assume a plank position with your hands placed slightly wider than shoulder-width apart. Lower your body by bending your elbows, keeping your body in a straight line. Push back up to the starting position.'},

        {'name': 'Pull-Ups',
         'info': 'Pull-ups are a challenging exercise that primarily work the back and biceps. They improve upper body strength and contribute to a balanced physique.',
         'how_to': 'Hang from a pull-up bar with your palms facing away from you. Pull your body upward by engaging your back muscles, and continue until your chin passes the bar. Lower yourself back down with control.'},

        {'name': 'Squats',
         'info': 'Squats are a foundational lower body exercise that work the thighs, hips, and buttocks. They help build lower body strength and improve overall leg stability.',
         'how_to': 'Stand with your feet shoulder-width apart. Lower your body by bending your knees and pushing your hips back, as if sitting in a chair. Keep your chest up and knees aligned with your toes. Return to the standing position by pushing through your heels.'},

        {'name': 'Deadlifts',
         'info': 'Deadlifts are a compound exercise that engage multiple muscle groups, including the back, legs, and arms. They contribute to overall strength and muscle development.',
         'how_to': 'Stand in front of a barbell with your feet hip-width apart. Bend at the hips and knees to grip the barbell with an overhand or mixed grip. Lift the barbell by extending your hips and standing up, then lower it back down with control.'},

        {'name': 'Bench Press',
         'info': 'The bench press is a classic chest exercise that also targets the shoulders and triceps. It\'s effective for building upper body strength and muscle.',
         'how_to': 'Lie on a flat bench and grip the barbell slightly wider than shoulder-width. Lower the bar to your chest, then press it back up to the starting position. Keep your feet flat on the floor for stability.'},

        {'name': 'Lunges',
         'info': 'Lunges are a versatile lower body exercise that work the thighs and buttocks. They also enhance balance and stability.',
         'how_to': 'Step forward with one leg and lower your body until both knees are bent at a 90-degree angle. Push back to the starting position and repeat on the other leg.'},

        {'name': 'Bicep Curls',
         'info': 'Bicep curls isolate the biceps and help build arm strength and definition. They are a popular exercise for targeting the front of the upper arms.',
         'how_to': 'Hold a dumbbell in each hand with your palms facing forward. Curl the dumbbells upward towards your shoulders, keeping your elbows close to your body. Lower the weights back down with control.'},

        {'name': 'Dips',
         'info': 'Dips are an effective triceps and shoulder exercise. They also engage the chest muscles and contribute to overall upper body strength.',
         'how_to': 'Hold onto parallel bars or a similar object with your arms fully extended. Lower your body by bending your elbows, then push yourself back up to the starting position.'},

        {'name': 'Leg Press',
         'info': 'The leg press machine targets the thighs and buttocks. It\'s a compound lower body exercise that allows you to lift heavier weights.',
         'how_to': 'Sit in a leg press machine and press the weight upwards using your legs. Extend your legs fully without locking your knees, then lower the weight back down with control.'},

        {'name': 'Overhead Press',
         'info': 'The overhead press targets the shoulders and triceps. It\'s effective for building shoulder strength and enhancing upper body muscular development.',
         'how_to': 'Hold a barbell or dumbbells at shoulder height. Press the weight upwards until your arms are fully extended, then lower it back down to shoulder level.'},

        {'name': 'Kettlebell Swings',
         'info': 'Kettlebell swings are a dynamic full-body exercise that primarily work the hips, glutes, hamstrings, and core. They also engage the lats, shoulders, and forearms.',
         'how_to': 'Hold a kettlebell with both hands and hinge at the hips. Swing the kettlebell between your legs, then thrust your hips forward to swing it to shoulder height. Allow the kettlebell to swing back down as you hinge at the hips again.'},

        {'name': 'Rows',
         'info': 'Rows are a back and shoulder exercise that help improve posture and upper body strength. They also engage the biceps and contribute to a well-rounded upper body workout.',
         'how_to': 'Hold a weight or barbell with an overhand grip. Pull the weight towards your lower chest while keeping your elbows close to your body. Squeeze your back muscles at the top of the movement.'},

        {'name': 'Box Jumps',
         'info': 'Box jumps are a plyometric exercise that work the legs and enhance explosive power. They are effective for improving athletic performance and lower body strength.',
         'how_to': 'Stand in front of a sturdy box or platform. Bend your knees and jump onto the box, landing softly with both feet. Step back down or jump back down to the starting position.'},

        {'name': 'Sit-Ups',
         'info': 'Sit-ups are a classic abdominal exercise that target the core muscles. They help build core strength and stability.',
         'how_to': 'Lie on your back with your knees bent and feet flat on the floor. Cross your arms over your chest or place your hands behind your head. Lift your upper body towards your knees, engaging your core. Lower back down with control.'},

        {'name': 'Plank',
         'info': 'The plank is an isometric exercise that primarily works the core muscles. It also engages the shoulders, arms, and glutes, promoting overall stability.',
         'how_to': 'Assume a push-up position with your hands directly under your shoulders and your body in a straight line from head to heels. Hold this position, engaging your core and maintaining proper alignment.'},

        {'name': 'Lat Pull-Downs',
         'info': 'Lat pull-downs target the back and shoulders. They help build upper body strength and improve posture.',
         'how_to': 'Sit at a lat pull-down machine and grip the bar with your palms facing away from you. Pull the bar down towards your chest, engaging your back muscles. Slowly release the bar back up to the starting position.'},

        {'name': 'Hammer Curls',
         'info': 'Hammer curls focus on the biceps and forearms. They provide a variation to standard bicep curls and contribute to arm strength and definition.',
         'how_to': 'Hold a dumbbell in each hand with your palms facing your body. Curl the dumbbells upward towards your shoulders, keeping your elbows close to your body. Lower the weights back down with control.'},

        {'name': 'Tricep Extensions',
         'info': 'Tricep extensions isolate the triceps muscles. They help build strength and definition in the back of the upper arms.',
         'how_to': 'Hold a dumbbell or barbell above your head with your arms fully extended. Bend your elbows to lower the weight behind your head, then extend your arms to lift it back up.'},

        {'name': 'Leg Curls',
         'info': 'Leg curls target the hamstrings. They contribute to overall leg strength and muscular balance.',
         'how_to': 'Lie face-down on a leg curl machine and curl your legs upwards against the resistance. Lower your legs back down with control.'},

        {'name': 'Chest Fly',
         'info': 'Chest fly exercises target the chest and shoulders. They help develop the pectoral muscles and enhance chest definition.',
         'how_to': 'Lie on a bench and hold a dumbbell in each hand above your chest, with your palms facing each other. Lower the weights in a wide arc until your arms are extended out to the sides, then squeeze your chest muscles to bring the weights back together.'},

        {'name': 'Lateral Raises',
         'info': 'Lateral raises work the shoulder muscles. They contribute to overall shoulder development and improve shoulder stability.',
         'how_to': 'Hold a dumbbell in each hand by your sides. Raise the dumbbells outward to shoulder level, keeping a slight bend in your elbows. Lower the weights back down with control.'},

        {'name': 'Calf Raises',
         'info': 'Calf raises target the calf muscles. They help improve calf strength and definition.',
         'how_to': 'Stand with the balls of your feet on an elevated surface and your heels hanging off the edge. Lift your heels as high as possible, then lower them back down below the level of the surface.'},

        {'name': 'T-Bar Rows',
         'info': 'T-bar rows target the back and shoulders. They are effective for building upper body strength and muscle.',
         'how_to': 'Place one end of a barbell into a landmine attachment or secure it in a corner. Load the other end with weight plates. Bend at the hips and knees, holding the bar with both hands. Pull the bar towards your lower chest while keeping your elbows close to your body. Squeeze your back muscles at the top of the movement.'},

        {'name': 'Face Pulls',
         'info': 'Face pulls primarily work the rear shoulders and upper traps. They contribute to balanced shoulder development and improved posture.',
         'how_to': 'Attach a rope handle to a cable machine at chest height. Hold the rope with an overhand grip and step back. Pull the rope towards your face, separating the ends as you pull. Focus on squeezing your rear shoulder muscles at the end of the movement.'},

        {'name': 'Shrugs',
         'info': 'Shrugs target the trapezius muscles. They help improve upper back strength and contribute to a well-developed upper body.',
         'how_to': 'Hold a dumbbell in each hand by your sides. Elevate your shoulders as high as possible by shrugging them upward. Lower your shoulders back down with control.'},
],

    'Flexibility': [
        {'name': 'Forward Fold',
         'info': 'The forward fold stretches the hamstrings and lower back. It\'s a calming pose that promotes flexibility.',
         'how_to': 'Stand straight, exhale, and bend forward from your hips. Keep your spine long and your knees slightly bent.'},

        {'name': 'Downward Dog',
         'info': 'Downward dog stretches the hamstrings, calves, and shoulders. It\'s a foundational yoga pose that also improves upper body strength.',
         'how_to': 'Start in a plank position and push your hips up towards the ceiling. Keep your hands shoulder-width apart and your feet hip-width apart. Press your heels towards the ground.'},

        {'name': 'Cobra Pose',
         'info': 'Cobra pose stretches the chest, shoulders, and abs. It helps open up the front of the body and improve posture.',
         'how_to': 'Lie face down and push your chest up off the floor while keeping your hips down. Keep your elbows slightly bent and gaze upwards.'},

        {'name': 'Seated Twist',
         'info': 'Seated twist stretches the spine and shoulders. It\'s a gentle twist that promotes spinal flexibility and digestion.',
         'how_to': 'Sit down, cross one leg over the other and twist your torso towards the crossed leg. Place your opposite hand on your outer thigh and the other hand behind you for support.'},

        {'name': 'Pigeon Pose',
         'info': 'Pigeon pose stretches the hips and lower back. It\'s a deep hip opener that helps release tension in the glutes and hip flexors.',
         'how_to': 'Start in a plank position and bring one knee forward, placing it behind your wrist. Extend your other leg back and lower your hips towards the ground.'},

        {'name': 'Butterfly Stretch',
         'info': 'Butterfly stretch stretches the inner thighs. It\'s a relaxing stretch that promotes flexibility in the hip area.',
         'how_to': 'Sit down, bring the soles of your feet together and push your knees towards the ground. Gently flap your knees up and down for a deeper stretch.'},

        {'name': 'Quad Stretch',
         'info': 'Quad stretch targets the quadriceps. It\'s an important stretch for maintaining balanced leg flexibility.',
         'how_to': 'Stand straight, grab one ankle and pull it towards your buttocks. Keep your knees together and your torso upright.'},

        {'name': 'Hip Flexor Stretch',
         'info': 'Hip flexor stretch stretches the hips and thighs. It helps alleviate tightness in the hip flexor muscles.',
         'how_to': 'Kneel down and step one foot forward, pushing your hips towards the ground. Keep your back straight and engage your core.'},

        {'name': 'Calf Stretch',
         'info': 'Calf stretch stretches the calves. It\'s important for maintaining flexible calf muscles.',
         'how_to': 'Step one foot back and push the heel into the ground. Keep your back leg straight and your front knee slightly bent.'},

        {'name': 'Child’s Pose',
         'info': 'Child’s pose stretches the back and arms. It\'s a restorative pose that promotes relaxation and releases tension.',
         'how_to': 'Kneel down and stretch your arms forward while lowering your chest towards the ground. Rest your forehead on the mat and sit back on your heels.'},

        {'name': 'Triangle Pose',
         'info': 'Triangle pose stretches the legs, hips, and spine. It\'s a standing pose that engages multiple muscle groups.',
         'how_to': 'Stand wide and extend one arm to the side, bending at the waist towards your extended hand. Keep your other arm reaching upwards.'},

        {'name': 'Bridge Pose',
         'info': 'Bridge pose stretches the chest and spine. It\'s a backbend that helps open the front of the body.',
         'how_to': 'Lie on your back and bend your knees, placing your feet flat on the ground. Push your hips towards the ceiling and interlace your fingers under your body.'},

        {'name': 'Cat-Cow',
         'info': 'Cat-cow stretches the spine and abs. It\'s a gentle flowing movement that promotes spinal flexibility.',
         'how_to': 'Start on all fours and alternate between arching and rounding your back. Inhale as you arch your back (cow pose), and exhale as you round your back (cat pose).'},

        {'name': 'Side Lunge',
         'info': 'Side lunge stretches the thighs and hips. It\'s a lateral stretch that also engages the inner thigh muscles.',
         'how_to': 'Stand wide and bend one knee, keeping the other leg straight. Shift your weight towards the bent knee and lean your torso in the same direction.'},

        {'name': 'Hamstring Stretch',
         'info': 'Hamstring stretch targets the hamstrings. It\'s important for maintaining flexible and healthy hamstrings.',
         'how_to': 'Sit down and extend one leg, reaching towards your toes. Keep your back straight and your chest open.'},

        {'name': 'Shoulder Stretch',
         'info': 'Shoulder stretch stretches the shoulders. It\'s important for maintaining shoulder mobility and reducing tension.',
         'how_to': 'Extend one arm across your body and use the other arm to pull it towards your chest. Keep your shoulder relaxed and avoid lifting your shoulder to your ear.'},

        {'name': 'Tricep Stretch',
         'info': 'Tricep stretch targets the triceps and shoulders. It helps release tension in the back of the upper arm.',
         'how_to': 'Raise one arm overhead and bend it, using the other hand to push it down towards your upper back. Gently hold the bent elbow with your other hand.'},

        {'name': 'Wrist Stretch',
         'info': 'Wrist stretch stretches the wrists and forearms. It\'s important for maintaining wrist flexibility and preventing discomfort.',
         'how_to': 'Extend one arm and use the other hand to pull the fingers downwards. Hold the stretch for a few seconds, then switch sides.'},

        {'name': 'Ankle Circles',
         'info': 'Ankle circles stretch the ankles. They help maintain ankle mobility and can relieve stiffness.',
         'how_to': 'Lift one foot and rotate the ankle in a circular motion. Perform clockwise and counterclockwise circles.'},

        {'name': 'Hip Circles',
         'info': 'Hip circles stretch the hips and lower back. They promote hip mobility and release tension.',
         'how_to': 'Stand straight and rotate your hips in a circular motion. Perform clockwise and counterclockwise circles.'},

        {'name': 'Neck Tilt',
         'info': 'Neck tilt stretches the neck. It\'s a gentle stretch that promotes neck flexibility and relaxation.',
         'how_to': 'Tilt your head to one side, trying to touch your ear to your shoulder. Hold the stretch for a few seconds, then switch to the other side.'},

        {'name': 'Spinal Twist',
         'info': 'Spinal twist stretches the spine. It helps improve spinal mobility and release tension in the back.',
         'how_to': 'Lie on your back and bring one knee across your body, keeping both shoulders on the ground. Gaze in the opposite direction of your bent knee.'},

        {'name': 'Knee to Chest',
         'info': 'Knee to chest stretch targets the lower back. It\'s a simple stretch that helps alleviate lower back tightness.',
         'how_to': 'Lie on your back and pull one knee towards your chest. Keep your other leg extended along the floor.'},

        {'name': 'Arm Circles',
         'info': 'Arm circles stretch the shoulders. They promote shoulder mobility and can be done as a warm-up or cool-down exercise.',
         'how_to': 'Extend your arms and rotate them in a circular motion. Perform small circles at first and gradually increase the size.'},

        {'name': 'Toe Touch',
         'info': 'Toe touch stretch stretches the hamstrings and lower back. It\'s a classic stretch that also promotes relaxation.',
         'how_to': 'Stand straight and reach down to touch your toes. Keep your knees slightly bent and your spine long.'},
],

        'Mental': [

        {'name': 'Cold Exposure',
        'info': 'Cold exposure involves intentionally exposing your body to cold temperatures, such as through cold showers or ice baths. This practice has been shown to offer a range of physical and mental benefits. When subjected to cold, your body responds by triggering hormonal changes, including an increase in norepinephrine, which can lead to heightened alertness, improved mood, and increased focus. Cold exposure also stimulates the activation of brown adipose tissue (BAT), commonly referred to as "brown fat," which plays a role in burning calories and supporting metabolism. Additionally, the practice of cold exposure can boost mental resilience, as it challenges your body and mind to adapt to uncomfortable conditions. Over time, this can lead to improved stress response and a greater ability to cope with challenging situations. Moreover, the practice of cold exposure can enhance motivation and discipline, as it requires you to overcome initial discomfort and step out of your comfort zone. \n\nWarning: Cold exposure can be intense and is not suitable for everyone. It\'s important to consider your age, fitness level, and any existing health conditions before attempting cold exposure. If you have a heart condition, respiratory issues, or other medical concerns, consult a healthcare professional before trying this exercise. Begin with gradual exposure and listen to your body. Stop immediately if you experience severe discomfort, numbness, or any adverse reactions.',
        'how_to': 'To engage in cold exposure, you can start by gradually incorporating cold showers into your routine. Begin with brief exposure to cold water at the end of your regular shower and then gradually increase the duration of cold exposure. For more intense cold exposure, consider immersing yourself in an ice bath for a short period of time. As you expose yourself to cold temperatures, focus on controlling your breath and remaining calm. Over time, you may find that the practice becomes more tolerable, and you experience the physical and mental benefits it offers.'},

            {
                'name': 'Mindfulness Meditation',
                'info': 'Mindfulness meditation involves focusing your attention on the present moment without judgment. By practicing mindfulness, you can increase your awareness of your thoughts, feelings, and sensations, while simultaneously reducing stress and promoting mental clarity.',
                'how_to': 'To practice mindfulness meditation, find a quiet and comfortable space. Sit down in a relaxed posture with your eyes closed. Direct your focus to your breath or a specific point of sensation. As thoughts arise, acknowledge them without judgment and gently bring your attention back to your breath or point of focus.'
            },
            {
                'name': 'Loving-Kindness Meditation',
                'info': 'Loving-kindness meditation, also known as Metta meditation, is a practice that involves cultivating feelings of compassion and love for oneself and others. By directing positive intentions towards yourself and others, you can enhance your sense of connection and emotional well-being.',
                'how_to': 'To engage in loving-kindness meditation, sit comfortably and close your eyes. Begin by silently reciting phrases of goodwill, such as "May I be happy, may I be healthy." After generating these feelings towards yourself, extend them to loved ones, acquaintances, and even those with whom you may have difficulties.'
            },
            {
                'name': 'Body Scan Meditation',
                'info': 'Body scan meditation is a technique that promotes relaxation and body awareness by systematically directing your attention to different parts of your body. This practice can help you release tension, connect with your body, and develop a deeper sense of presence.',
                'how_to': 'To practice body scan meditation, lie down or sit in a comfortable position. Close your eyes and begin to bring your awareness to different parts of your body, starting from your toes and gradually moving upwards. Notice any sensations, tension, or relaxation in each area as you focus on it.'
            },
            {
                'name': 'Breath Awareness Meditation',
                'info': 'Breath awareness meditation involves directing your attention to the rhythm of your breath. This practice can help you stay anchored in the present moment, calm your mind, and develop a greater sense of self-awareness.',
                'how_to': 'Sit or lie down comfortably in a quiet space. Close your eyes and bring your attention to your breath. Observe the natural flow of your breath as you inhale and exhale. If your mind starts to wander, gently guide your focus back to your breath.'
            },
            {
                'name': 'Transcendental Meditation',
                'info': 'Transcendental meditation is a popular technique that involves silently repeating a specific mantra. This practice aims to lead you to a state of deep relaxation and restful awareness, allowing you to access a quieter and more peaceful level of consciousness.',
                'how_to': 'To practice transcendental meditation, sit with your eyes closed and silently repeat a chosen mantra. Allow your breath to become slow and steady as you continue to repeat the mantra in your mind. Whenever your attention drifts, gently bring it back to the mantra.'
            },
            {
                'name': 'Visualization Meditation',
                'info': 'Visualization meditation involves creating and immersing yourself in a mental image of a peaceful place or scenario. By engaging your senses and imagination, this practice can help you relax, reduce stress, and cultivate positive emotions.',
                'how_to': 'To engage in visualization meditation, find a quiet space and sit or lie down comfortably. Close your eyes and imagine a serene place, such as a beach or a meadow. Visualize every detail, including colors, sounds, and textures.'
            },
            {
                'name': 'Chakra Meditation',
                'info': 'Chakra meditation draws from ancient Indian practices and focuses on energy centers (chakras) within the body. By directing your attention to these energy points, you can promote balance, alignment, and a sense of harmony.',
                'how_to': 'To practice chakra meditation, sit comfortably and close your eyes. Begin by directing your attention to the base of your spine, imagining a spinning wheel of energy. Gradually move your focus to each successive chakra, moving upwards.'
            },
            {
                'name': 'Walking Meditation',
                'info': 'Walking meditation combines the practice of meditation with mindful walking. By paying attention to each step and your surroundings, you can cultivate mindfulness, enhance focus, and integrate meditation into your daily movement.',
                'how_to': 'To engage in walking meditation, find a quiet outdoor space with a clear path. Walk slowly and deliberately, paying attention to each step. Notice the sensation of your feet touching the ground and the rhythm of your breath.'
            },
            {
                'name': 'Body Movement Meditation',
                'info': 'Body movement meditation combines gentle movements with meditation, promoting body awareness, relaxation, and a sense of presence. This practice encourages you to connect your breath with your movements and fully experience the sensations of your body.',
                'how_to': 'To practice body movement meditation, stand or sit in a comfortable position. Move your body slowly and mindfully, coordinating each movement with your breath. Pay attention to the sensations, stretches, and flows of energy in your body.'
            },
            {
                'name': 'Breath Counting Meditation',
                'info': 'Breath counting meditation involves counting your breaths to a specific number. By focusing on the rhythm of your breath and the act of counting, you can enhance concentration, promote mindfulness, and quiet your mind.',
                'how_to': 'To engage in breath counting meditation, sit comfortably and close your eyes. Inhale deeply and count "one." Exhale fully and count "two." Continue this pattern until you reach a predetermined count. If your mind wanders, gently bring your focus back to the breath and counting.'
            },
            # Add more exercises as needed
]

}



# Add the title above everything
Label(root, text="Workout Planner", font=("Arial", 18, "bold")).grid(row=0, columnspan=3, pady=20)

# Create frames for each category and populate with exercises
frames = {}
col_idx = 0
for category, exercises in category_exercises.items():
    frame = Frame(root)
    frame.grid(row=1, column=col_idx, padx=15, pady=10)
    frames[category] = frame

    Label(frame, text=category, font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=10, sticky=W + E)

    # Adding labels for Sets, Reps, Duration, and Weight with 5-character spacing
    Label(frame, text="Sets").grid(row=1, column=2)
    Label(frame, text="Reps").grid(row=1, column=4)
    Label(frame, text="Duration").grid(row=1, column=6)
    Label(frame, text="Weight").grid(row=1, column=8)

    row_idx = 2
    for exercise in exercises:
        input_boxes = create_input_boxes(frame, row_idx)

        Checkbutton(frame, text=exercise['name'], variable=input_boxes['var']).grid(row=row_idx, column=0, sticky=W)
        exercise_inputs[exercise['name']] = input_boxes

        Button(frame, text="i", command=lambda exercise=exercise: show_info(exercise['info'], exercise['how_to'])).grid(
            row=row_idx, column=1)

        row_idx += 1

    col_idx += 1

# Dropdown for selecting the day
day_var = StringVar()
day_var.set("Select Day")
day_dropdown = OptionMenu(root, day_var, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
day_dropdown.grid(row=2, column=0, pady=10)
day_dropdown.config(width=9)  # Set to the width of the text

# Center-align the dropdown and button
day_dropdown.grid(row=2, column=0, pady=10, columnspan=3)
# The save button
save_button = Button(root, text="Save Workout", command=save_workout_program)
save_button.grid(row=7, column=0, pady=10, columnspan=3)

root.mainloop()