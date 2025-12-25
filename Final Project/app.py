from flask import Flask, render_template, request, jsonify, session
import random
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Game data
VILLAINS = ["Tomura Shigaraki", "Kurogiri", "Dabi", "Himiko Toga", "Stain"]
LOCATIONS = ["U.A. High School", "Kamino Ward", "Hosu City", "Musutafu City", "Kiyashi Ward"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    data = request.json
    hero_name = data.get('hero_name', 'Hero')
    
    session['hero_name'] = hero_name
    session['hero_xp'] = 0
    session['hero_level'] = 1
    session['battles_won'] = 0
    
    return jsonify({
        'success': True,
        'hero_name': hero_name,
        'message': f'Welcome, {hero_name}! Your hero journey begins!'
    })

@app.route('/explore', methods=['POST'])
def explore():
    hero_name = session.get('hero_name', 'Hero')
    location = random.choice(LOCATIONS)
    villain = random.choice(VILLAINS)
    
    session['current_villain'] = villain
    session['current_location'] = location
    session['villain_health'] = random.randint(50, 100)
    session['hero_health'] = 100
    
    return jsonify({
        'success': True,
        'location': location,
        'villain': villain,
        'message': f'{hero_name} is exploring {location}...',
        'villain_health': session['villain_health'],
        'hero_health': session['hero_health']
    })

@app.route('/battle', methods=['POST'])
def battle():
    data = request.json
    action = data.get('action')
    
    hero_name = session.get('hero_name', 'Hero')
    hero_level = session.get('hero_level', 1)
    villain_name = session.get('current_villain', 'Villain')
    
    hero_health = session.get('hero_health', 100)
    villain_health = session.get('villain_health', 100)
    
    battle_log = []
    
    # Hero's action
    if action == 'quirk':
        hero_attack = random.randint(10, 20) + hero_level
        villain_health -= hero_attack
        battle_log.append(f'{hero_name} uses their Quirk! Deals {hero_attack} damage!')
    elif action == 'evade':
        critical_evasion_chance = random.random()
        if critical_evasion_chance <= 0.2:
            hero_attack = random.randint(5, 15)
            villain_health -= hero_attack
            battle_log.append(f'{hero_name} evades and counters! Deals {hero_attack} damage!')
        else:
            battle_log.append(f'{hero_name} tried to evade but failed!')
    elif action == 'heal':
        healing_amount = random.randint(15, 25)
        hero_health = min(100, hero_health + healing_amount)
        battle_log.append(f'{hero_name} uses a Healing Item! Restores {healing_amount} HP!')
    
    # Check if villain is defeated
    if villain_health <= 0:
        xp_earned = random.randint(20, 40)
        session['hero_xp'] = session.get('hero_xp', 0) + xp_earned
        session['battles_won'] = session.get('battles_won', 0) + 1
        
        new_level = session['hero_xp'] // 100 + 1
        leveled_up = new_level > session.get('hero_level', 1)
        session['hero_level'] = new_level
        
        return jsonify({
            'success': True,
            'battle_over': True,
            'victory': True,
            'battle_log': battle_log,
            'xp_earned': xp_earned,
            'total_xp': session['hero_xp'],
            'hero_level': new_level,
            'leveled_up': leveled_up,
            'hero_health': hero_health,
            'villain_health': 0,
            'can_fight_boss': new_level >= 10
        })
    
    # Villain's turn
    if action != 'heal':
        villain_attack = random.randint(10, 20) + hero_level
        hero_health -= villain_attack
        battle_log.append(f'{villain_name} attacks! Deals {villain_attack} damage!')
    
    # Check if hero is defeated
    if hero_health <= 0:
        return jsonify({
            'success': True,
            'battle_over': True,
            'victory': False,
            'battle_log': battle_log,
            'hero_health': 0,
            'villain_health': villain_health
        })
    
    # Update session
    session['hero_health'] = hero_health
    session['villain_health'] = villain_health
    
    return jsonify({
        'success': True,
        'battle_over': False,
        'battle_log': battle_log,
        'hero_health': hero_health,
        'villain_health': villain_health
    })

@app.route('/final_boss', methods=['POST'])
def final_boss():
    data = request.json
    action = data.get('action')
    
    hero_name = session.get('hero_name', 'Hero')
    hero_level = session.get('hero_level', 1)
    boss_name = "All For One"
    
    # Initialize boss battle if not already started
    if 'boss_health' not in session:
        session['boss_health'] = 150 + hero_level * 2
        session['hero_health'] = 100
    
    hero_health = session.get('hero_health', 100)
    boss_health = session.get('boss_health', 150)
    
    battle_log = []
    
    # Hero's action
    if action == 'ultimate':
        hero_attack = random.randint(20, 30) + hero_level
        boss_health -= hero_attack
        battle_log.append(f'{hero_name} uses Ultimate Quirk! Deals {hero_attack} damage!')
    elif action == 'teamup':
        team_attack = random.randint(15, 25) + hero_level
        boss_health -= team_attack
        battle_log.append(f'{hero_name} and allies use Team-Up Attack! Deals {team_attack} damage!')
    elif action == 'heal':
        healing_amount = random.randint(20, 30)
        hero_health = min(100, hero_health + healing_amount)
        battle_log.append(f'{hero_name} uses a Healing Item! Restores {healing_amount} HP!')
    
    # Check if boss is defeated
    if boss_health <= 0:
        # Clear boss battle session
        session.pop('boss_health', None)
        return jsonify({
            'success': True,
            'battle_over': True,
            'victory': True,
            'battle_log': battle_log,
            'hero_health': hero_health,
            'boss_health': 0,
            'message': f'Congratulations! {hero_name} defeated {boss_name} and saved the world!'
        })
    
    # Boss's turn
    boss_attack = random.randint(15, 30) + hero_level
    hero_health -= boss_attack
    battle_log.append(f'{boss_name} attacks with devastating power! Deals {boss_attack} damage!')
    
    # Check if hero is defeated
    if hero_health <= 0:
        session.pop('boss_health', None)
        return jsonify({
            'success': True,
            'battle_over': True,
            'victory': False,
            'battle_log': battle_log,
            'hero_health': 0,
            'boss_health': boss_health,
            'message': f'{hero_name} was defeated by {boss_name}. The world falls into darkness...'
        })
    
    # Update session
    session['hero_health'] = hero_health
    session['boss_health'] = boss_health
    
    return jsonify({
        'success': True,
        'battle_over': False,
        'battle_log': battle_log,
        'hero_health': hero_health,
        'boss_health': boss_health
    })

@app.route('/stats')
def stats():
    return jsonify({
        'hero_name': session.get('hero_name', 'Hero'),
        'hero_level': session.get('hero_level', 1),
        'hero_xp': session.get('hero_xp', 0),
        'battles_won': session.get('battles_won', 0)
    })

if __name__ == '__main__':
    app.run(debug=True)
