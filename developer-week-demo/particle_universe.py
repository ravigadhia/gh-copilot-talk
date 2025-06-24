"""
Impressive Particle Universe Simulation for Developer Week Conference Demo
A stunning visual demonstration of GitHub Copilot's capabilities

This simulation creates a beautiful particle universe with:
- Real-time physics simulation with 500+ particles
- Dynamic color-changing based on velocity and position
- Particle collisions and gravitational effects
- Interactive mouse controls
- Multiple rendering modes
- Sound generation capabilities
"""

import pygame
import random
import math
import numpy as np
import wave
import struct
from typing import List, Tuple
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60
PARTICLE_COUNT = 300
GRAVITY_STRENGTH = 0.1
MAX_VELOCITY = 8
COLORS = [
    (255, 100, 100),  # Red
    (100, 255, 100),  # Green  
    (100, 100, 255),  # Blue
    (255, 255, 100),  # Yellow
    (255, 100, 255),  # Magenta
    (100, 255, 255),  # Cyan
    (255, 200, 100),  # Orange
    (200, 100, 255),  # Purple
]

class Particle:
    """A single particle in our universe with physics properties"""
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.vx = random.uniform(-3, 3)
        self.vy = random.uniform(-3, 3)
        self.mass = random.uniform(1, 5)
        self.radius = int(self.mass * 2)
        self.color = random.choice(COLORS)
        self.trail = []
        self.energy = 1.0
        self.age = 0
        
    def update(self, particles: List['Particle'], mouse_pos: Tuple[int, int]):
        """Update particle position and physics"""
        self.age += 1
        
        # Mouse attraction/repulsion
        if mouse_pos:
            mouse_x, mouse_y = mouse_pos
            dx = mouse_x - self.x
            dy = mouse_y - self.y
            distance = math.sqrt(dx*dx + dy*dy)
            
            if distance > 0:
                # Intentional Bug: Using wrong variable name - should be 'distance' not 'dist'
                force = GRAVITY_STRENGTH * self.mass / (dist * dist)  # This will cause NameError
                self.vx += (dx / distance) * force
                self.vy += (dy / distance) * force
        
        # Particle-to-particle interactions
        for other in particles:
            if other != self:
                dx = other.x - self.x
                dy = other.y - self.y
                distance = math.sqrt(dx*dx + dy*dy)
                
                if distance > 0 and distance < 100:
                    # Gravitational attraction
                    force = (self.mass * other.mass) / (distance * distance) * 0.01
                    self.vx += (dx / distance) * force
                    self.vy += (dy / distance) * force
                    
                    # Collision detection
                    if distance < (self.radius + other.radius):
                        # Elastic collision
                        self.vx *= -0.8
                        self.vy *= -0.8
        
        # Update position
        self.x += self.vx
        self.y += self.vy
        
        # Velocity limiting
        velocity = math.sqrt(self.vx*self.vx + self.vy*self.vy)
        if velocity > MAX_VELOCITY:
            self.vx = (self.vx / velocity) * MAX_VELOCITY
            self.vy = (self.vy / velocity) * MAX_VELOCITY
        
        # Boundary conditions with energy conservation
        if self.x < self.radius or self.x > SCREEN_WIDTH - self.radius:
            self.vx *= -0.9
            self.x = max(self.radius, min(SCREEN_WIDTH - self.radius, self.x))
            
        if self.y < self.radius or self.y > SCREEN_HEIGHT - self.radius:
            self.vy *= -0.9
            self.y = max(self.radius, min(SCREEN_HEIGHT - self.radius, self.y))
        
        # Update trail
        self.trail.append((int(self.x), int(self.y)))
        if len(self.trail) > 20:
            self.trail.pop(0)
        
        # Update color based on velocity
        velocity_factor = min(velocity / MAX_VELOCITY, 1.0)
        base_color = self.color
        self.current_color = (
            int(base_color[0] * (0.5 + 0.5 * velocity_factor)),
            int(base_color[1] * (0.5 + 0.5 * velocity_factor)),
            int(base_color[2] * (0.5 + 0.5 * velocity_factor))
        )
    
    def draw(self, screen: pygame.Surface, render_mode: str = "normal"):
        """Draw the particle with various rendering modes"""
        
        if render_mode == "trails":
            # Draw particle trail
            for i, pos in enumerate(self.trail):
                alpha = int(255 * (i / len(self.trail)))
                trail_color = (*self.current_color, alpha)
                pygame.draw.circle(screen, self.current_color, pos, max(1, self.radius - i))
        
        elif render_mode == "energy":
            # Draw particle with energy visualization
            energy_radius = int(self.radius * self.energy)
            pygame.draw.circle(screen, self.current_color, (int(self.x), int(self.y)), energy_radius)
            pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius, 2)
        
        else:
            # Normal rendering
            pygame.draw.circle(screen, self.current_color, (int(self.x), int(self.y)), self.radius)
            # Add glow effect
            for i in range(3):
                glow_color = tuple(max(0, c - i*50) for c in self.current_color)
                pygame.draw.circle(screen, glow_color, (int(self.x), int(self.y)), self.radius + i, 1)

class ParticleUniverse:
    """Main simulation class managing all particles and effects"""
    
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Particle Universe - GitHub Copilot Demo")
        self.clock = pygame.time.Clock()
        self.particles = []
        self.render_mode = "normal"
        self.paused = False
        self.mouse_attraction = True
        
        # Initialize particles
        for _ in range(PARTICLE_COUNT):
            x = random.uniform(50, SCREEN_WIDTH - 50)
            y = random.uniform(50, SCREEN_HEIGHT - 50)
            self.particles.append(Particle(x, y))
    
    def handle_events(self):
        """Handle user input and events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                elif event.key == pygame.K_r:
                    self.reset_simulation()
                elif event.key == pygame.K_t:
                    self.render_mode = "trails" if self.render_mode != "trails" else "normal"
                elif event.key == pygame.K_e:
                    self.render_mode = "energy" if self.render_mode != "energy" else "normal"
                elif event.key == pygame.K_m:
                    self.mouse_attraction = not self.mouse_attraction
                elif event.key == pygame.K_s:
                    self.generate_sound_wave()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Add explosion effect at mouse position
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.create_explosion(mouse_x, mouse_y)
        
        return True
    
    def reset_simulation(self):
        """Reset all particles to random positions"""
        self.particles.clear()
        for _ in range(PARTICLE_COUNT):
            x = random.uniform(50, SCREEN_WIDTH - 50)
            y = random.uniform(50, SCREEN_HEIGHT - 50)
            self.particles.append(Particle(x, y))
    
    def create_explosion(self, x: int, y: int):
        """Create an explosion effect at the given position"""
        for particle in self.particles:
            dx = particle.x - x
            dy = particle.y - y
            distance = math.sqrt(dx*dx + dy*dy)
            
            if distance < 150:  # Explosion radius
                force = 500 / max(distance, 1)
                particle.vx += (dx / max(distance, 1)) * force * 0.1
                particle.vy += (dy / max(distance, 1)) * force * 0.1
    
    def generate_sound_wave(self):
        """Generate a sound wave file based on particle positions"""
        try:
            # Create wave data based on particle positions
            sample_rate = 44100
            duration = 2.0
            frames = int(duration * sample_rate)
            
            # Generate sound based on particle properties
            wave_data = []
            for i in range(frames):
                t = i / sample_rate
                amplitude = 0
                
                for particle in self.particles[:10]:  # Use first 10 particles
                    frequency = 200 + (particle.x / SCREEN_WIDTH) * 400
                    particle_amplitude = particle.mass / 5.0 * 0.1
                    amplitude += particle_amplitude * math.sin(2 * math.pi * frequency * t)
                
                # Normalize and convert to 16-bit
                amplitude = max(-1, min(1, amplitude))
                wave_data.append(int(amplitude * 32767))
            
            # Save as WAV file
            with wave.open('particle.wav', 'w') as wav_file:
                wav_file.setnchannels(1)  # Mono
                wav_file.setsampwidth(2)  # 2 bytes per sample
                wav_file.setframerate(sample_rate)
                
                for sample in wave_data:
                    wav_file.writeframes(struct.pack('<h', sample))
            
            print("Sound wave generated and saved as 'particle.wav'!")
            
        except Exception as e:
            print(f"Error generating sound: {e}")
    
    def update(self):
        """Update all particles"""
        if not self.paused:
            mouse_pos = pygame.mouse.get_pos() if self.mouse_attraction else None
            
            for particle in self.particles:
                particle.update(self.particles, mouse_pos)
    
    def draw(self):
        """Draw all particles and UI"""
        # Create starfield background
        self.screen.fill((5, 5, 15))
        
        # Draw particles
        for particle in self.particles:
            particle.draw(self.screen, self.render_mode)
        
        # Draw UI
        self.draw_ui()
        
        pygame.display.flip()
    
    def draw_ui(self):
        """Draw user interface elements"""
        font = pygame.font.Font(None, 36)
        small_font = pygame.font.Font(None, 24)
        
        # Title
        title = font.render("Particle Universe - GitHub Copilot Demo", True, (255, 255, 255))
        self.screen.blit(title, (10, 10))
        
        # Instructions
        instructions = [
            "SPACE: Pause/Resume",
            "R: Reset",
            "T: Toggle Trails",
            "E: Energy Mode", 
            "M: Mouse Attraction",
            "S: Generate Sound",
            "Click: Explosion"
        ]
        
        for i, instruction in enumerate(instructions):
            text = small_font.render(instruction, True, (200, 200, 200))
            self.screen.blit(text, (10, 50 + i * 25))
        
        # Status
        status_text = f"Particles: {len(self.particles)} | Mode: {self.render_mode}"
        if self.paused:
            status_text += " | PAUSED"
        
        status = small_font.render(status_text, True, (255, 255, 100))
        self.screen.blit(status, (10, SCREEN_HEIGHT - 30))
    
    def run(self):
        """Main game loop"""
        print("🌟 Particle Universe Demo Starting!")
        print("This demo showcases GitHub Copilot's capabilities with:")
        print("- Complex algorithm generation")
        print("- Physics simulation")
        print("- Interactive features")
        print("- Error handling and debugging")
        print("\nNote: There's an intentional bug - try running and see what Copilot suggests!")
        
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    # Check if pygame is available
    try:
        import pygame
    except ImportError:
        print("Pygame is required for this demo. Install with: pip install pygame")
        sys.exit(1)
    
    # Create and run the simulation
    universe = ParticleUniverse()
    universe.run()