// Testimonial Carousel JavaScript
class TestimonialCarousel {
    constructor(options = {}) {
        this.currentIndex = 0;
        this.items = [];
        this.autoPlay = options.autoPlay !== false;
        this.interval = options.interval || 5000;
        this.container = null;
        this.prevBtn = null;
        this.nextBtn = null;
        this.indicators = [];
        this.intervalId = null;
        
        this.init();
    }
    
    init() {
        this.createCarouselStructure();
        this.bindEvents();
        this.startAutoScroll();
    }
    
    createCarouselStructure() {
        // Create testimonial section if it doesn't exist
        this.createSection();
    }
    
    createSection() {
        const existingSection = document.querySelector('.testimonial-carousel-container');
        if (existingSection) return;
        
        // Find insertion point - after services section
        const servicesSection = document.querySelector('.elementor-element-f02bc2b')?.closest('.elementor-section');
        const contactSection = document.querySelector('.elementor-element-001')?.closest('.elementor-section');
        
        // Create testimonial section HTML
        const testimonialHTML = `
            <section class="elementor-section elementor-top-section elementor-element-testimonials elementor-section-boxed elementor-section-height-default" data-e-type="section" data-element_type="section" data-settings='{"background_background":"classic"}'>
                <div class="elementor-container elementor-column-gap-default">
                    <div class="elementor-column elementor-col-100 elementor-top-column" data-e-type="column" data-element_type="column">
                        <div class="elementor-widget-wrap elementor-element-populated">
                            
                            <div class="elementor-element de_scroll_animation_no elementor-invisible" data-e-type="widget" data-element_type="widget" data-settings='{"_animation":"fadeIn","_animation_delay":200}'>
                                <div class="elementor-widget-container">
                                    <div class="ekit-wid-con">
                                        <div class="ekit-heading elementskit-section-title-wraper text_center">
                                            <h2 class="ekit-heading--title elementskit-section-title">What Our Clients Say</h2>
                                            <p class="elementskit-section-subtitle">Real stories from real people who found balance</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="testimonial-carousel-container">
                                ${this.createTestimonialItems()}
                                
                                <div class="testimonial-navigation">
                                    <button class="carousel-btn prev-btn" aria-label="Previous testimonial">
                                        <i class="fas fa-chevron-left"></i>
                                    </button>
                                    
                                    <div class="carousel-indicators">
                                        <span class="indicator active" data-index="0" aria-label="Testimonial 1"></span>
                                        <span class="indicator" data-index="1" aria-label="Testimonial 2"></span>
                                        <span class="indicator" data-index="2" aria-label="Testimonial 3"></span>
                                        <span class="indicator" data-index="3" aria-label="Testimonial 4"></span>
                                        <span class="indicator" data-index="4" aria-label="Testimonial 5"></span>
                                    </div>
                                    
                                    <button class="carousel-btn next-btn" aria-label="Next testimonial">
                                        <i class="fas fa-chevron-right"></i>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <link rel="stylesheet" href="assets/css/testimonial-carousel.css">
        `;
        
        // Insert after services section or at the end of main content
        if (servicesSection && servicesSection.nextElementSibling) {
            servicesSection.insertAdjacentHTML('afterend', testimonialHTML);
        } else {
            const mainContent = document.querySelector('#main-content') || document.querySelector('#content');
            if (mainContent) {
                mainContent.insertAdjacentHTML('beforeend', testimonialHTML);
            }
        }
        
        // Initialize carousel elements
        this.container = document.querySelector('.testimonial-carousel-container');
        this.initializeElements();
    }
    
    createTestimonialItems() {
        const testimonials = [
            {
                text: "Dr. Teena helped me navigate through my anxiety and depression with compassion and expertise. The sessions provided me with practical tools to manage my mental health effectively.",
                name: "Sarah M.",
                role: "Individual Counseling Client",
                icon: "icon2_3.png"
            },
            {
                text: "The support group sessions were life-changing. Connecting with others who understand my struggles made me feel less alone and more empowered to tackle my challenges.",
                name: "Michael R.",
                role: "Support Group Member",
                icon: "icon2_7.png"
            },
            {
                text: "Working with Dr. Teena gave me the tools to understand my triggers and develop healthier coping strategies. I am now better equipped to manage my daily stress and anxiety.",
                name: "Priya K.",
                role: "Anxiety & Mood Therapy Client",
                icon: "icon2_6.png"
            },
            {
                text: "As a therapist in training, the mentorship provided through Being Balanced was invaluable. Dr. Teena's guidance helped me develop confidence and professional skills.",
                name: "Arjun S.",
                role: "Mentorship Program Client",
                icon: "icon2_4.png"
            },
            {
                text: "The couple counseling sessions helped us understand each other better and improved our communication significantly. We now have tools to navigate challenging situations together.",
                name: "Rina & Rajan", 
                role: "Couple Therapy Clients",
                icon: "icon2_9.png"
            }
        ];
        
        return testimonials.map((testimonial, index) => `
            <div class="testimonial-item ${index === 0 ? 'active' : ''}" data-index="${index}">
                <div class="testimonial-content">
                    <div class="quote-icon">
                        <i class="fas fa-quote-left"></i>
                    </div>
                    <p class="testimonial-text">${testimonial.text}</p>
                    <div class="testimonial-author">
                        <img src="images/${testimonial.icon}" alt="${testimonial.name}" onerror="this.src='images/icon2_3.png'" class="author-image">
                        <div class="author-info">
                            <h4>${testimonial.name}</h4>
                            <span>${testimonial.role}</span>
                        </div>
                    </div>
                </div>
            </div>
        `).join('');
    }
    
    initializeElements() {
        if (!this.container) return;
        
        this.items = this.container.querySelectorAll('.testimonial-item');
        this.prevBtn = this.container.querySelector('.prev-btn');
        this.nextBtn = this.container.querySelector('.next-btn');
        this.indicators = this.container.querySelectorAll('.indicator');
    }
    
    bindEvents() {
        if (!this.container) return;
        
        // Click events
        this.prevBtn?.addEventListener('click', () => this.previous());
        this.nextBtn?.addEventListener('click', () => this.next());
        
        this.indicators.forEach((indicator, index) => {
            indicator.addEventListener('click', () => this.goTo(index));
        });
        
        // Touch/swipe events
        let startX = 0;
        let endX = 0;
        
        const carousel = this.container.querySelector('.testimonial-carousel-wrapper');
        if (carousel) {
            carousel.addEventListener('touchstart', (e) => {
                startX = e.touches[0].clientX;
            });
            
            carousel.addEventListener('touchend', (e) => {
                endX = e.changedTouches[0].clientX;
                this.handleSwipe();
            });
            
            // Pause on hover
            this.container.addEventListener('mouseenter', () => this.pause());
            this.container.addEventListener('mouseleave', () => this.startAutoScroll());
        }
        
        // Keyboard navigation
        document.addEventListener('keydown', (e) => {
            if (e.target.closest('.testimonial-carousel-container')) {
                switch(e.key) {
                    case 'ArrowLeft':
                        this.previous();
                        break;
                    case 'ArrowRight':
                        this.next();
                        break;
                }
            }
        });
        
        // Focus management for accessibility
        this.addFocusSupport();
    }
    
    handleSwipe() {
        const threshold = 50;
        const difference = startX - endX;
        
        if (Math.abs(difference) > threshold) {
            if (difference > 0) {
                this.next();
            } else {
                this.previous();
            }
        }
    }
    
    addFocusSupport() {
        const carousel = this.container?.querySelector('.testimonial-carousel-wrapper');
        if (carousel) {
            carousel.setAttribute('tabindex', '0');
            carousel.setAttribute('role', 'region');
            carousel.setAttribute('aria-label', 'Client testimonials carousel');
            
            // Announce current testimonial for screen readers
            const announcement = document.createElement('div');
            announcement.className = 'sr-only';
            announcement.setAttribute('aria-live', 'polite');
            carousel.appendChild(announcement);
        }
    }
    
    next() {
        this.currentIndex = (this.currentIndex + 1) % this.items.length;
        this.updateDisplay();
    }
    
    previous() {
        this.currentIndex = (this.currentIndex - 1 + this.items.length) % this.items.length;
        this.updateDisplay();
    }
    
    goTo(index) {
        this.currentIndex = index;
        this.updateDisplay();
    }
    
    updateDisplay() {
        // Update items
        this.items.forEach((item, index) => {
            item.classList.toggle('active', index === this.currentIndex);
            
            // Announce current for screen readers
            if (index === this.currentIndex) {
                const name = item.querySelector('.author-info h4')?.textContent;
                const role = item.querySelector('.author-info span')?.textContent;
                
                const announcement = this.container?.querySelector('.sr-only');
                if (announcement) {
                    announcement.textContent = `Testimonial by ${name}, ${role}`;
                }
            }
        });
        
        // Update indicators
        this.indicators.forEach((indicator, index) => {
            indicator.classList.toggle('active', index === this.currentIndex);
            indicator.setAttribute('aria-current', index === this.currentIndex ? 'true' : 'false');
        });
    }
    
    startAutoScroll() {
        if (this.autoPlay && !this.intervalId) {
            this.intervalId = setInterval(() => {
                this.next();
            }, this.interval);
        }
    }
    
    pause() {
        if (this.intervalId) {
            clearInterval(this.intervalId);
            this.intervalId = null;
        }
    }
    
    stop() {
        this.pause();
    }
    
    resume() {
        this.startAutoScroll();
    }
    
    destroy() {
        this.stop();
        // Remove event listeners and clean up
        if (this.container) {
            this.container.removeEventListener('mouseenter', () => this.pause());
            this.container.removeEventListener('mouseleave', () => this.startAutoScroll());
        }
    }
}

// Initialize the carousel when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Load Font Awesome if not already loaded
    if (!document.querySelector('[data-font-awesome]')) {
        const fontAwesome = document.createElement('link');
        fontAwesome.rel = 'stylesheet';
        fontAwesome.href = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css';
        fontAwesome.setAttribute('data-font-awesome', 'true');
        document.head.appendChild(fontAwesome);
    }
    
    // Load custom CSS if not loaded
    if (!document.querySelector('#testimonial-carousel-styles')) {
        const styles = document.createElement('link');
        styles.id = 'testimonial-carousel-styles';
        styles.rel = 'stylesheet';
        styles.href = 'assets/css/testimonial-carousel.css';
        document.head.appendChild(styles);
    }
    
    const carousel = new TestimonialCarousel({
        autoPlay: true,
        interval: 6000
    });
    
    // Make it globally accessible
    window.testimonialCarousel = carousel;
});

// Fallback compatibility
if (typeof module !== 'undefined' && module.exports) {
    module.exports = TestimonialCarousel;
}