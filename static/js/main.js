// Advanced Paper Generator Client-Side Features
class PaperGenerator {
    constructor() {
        this.currentPaper = null;
        this.autoSaveInterval = null;
        this.templates = [];
        this.init();
    }
    
    init() {
        this.loadTemplates();
        this.setupAutoSave();
        this.setupKeyboardShortcuts();
        this.setupRealTimePreview();
    }
    
    // Real-time topic suggestions
    async getTopicSuggestions(query) {
        if (query.length < 3) return [];
        
        try {
            const response = await fetch(`/api/suggest-topics?q=${encodeURIComponent(query)}`);
            const data = await response.json();
            return data.suggestions || [];
        } catch (error) {
            console.error('Error fetching suggestions:', error);
            return [];
        }
    }
    
    // Smart templates
    async loadTemplates() {
        try {
            const response = await fetch('/paper/templates');
            const data = await response.json();
            this.templates = data.templates;
            this.renderTemplateSelector();
        } catch (error) {
            console.error('Error loading templates:', error);
        }
    }
    
    renderTemplateSelector() {
        const container = document.getElementById('templateContainer');
        if (!container) return;
        
        let html = '<div class="row g-3">';
        this.templates.forEach(template => {
            html += `
                <div class="col-md-4">
                    <div class="card template-card h-100" onclick="selectTemplate('${template.id}')">
                        <div class="card-body text-center">
                            <h5 class="card-title">${template.name}</h5>
                            <p class="card-text text-muted">${template.description}</p>
                        </div>
                    </div>
                </div>
            `;
        });
        html += '</div>';
        container.innerHTML = html;
    }
    
    // Auto-save functionality
    setupAutoSave() {
        this.autoSaveInterval = setInterval(() => {
            if (this.currentPaper) {
                this.saveToDraft();
            }
        }, 30000); // Auto-save every 30 seconds
    }
    
    saveToDraft() {
        const draft = {
            ...this.currentPaper,
            timestamp: Date.now(),
            id: this.currentPaper.id || this.generateId()
        };
        
        localStorage.setItem(`draft_${draft.id}`, JSON.stringify(draft));
        this.showNotification('Draft saved automatically', 'info');
    }
    
    loadDrafts() {
        const drafts = [];
        for (let i = 0; i < localStorage.length; i++) {
            const key = localStorage.key(i);
            if (key.startsWith('draft_')) {
                try {
                    const draft = JSON.parse(localStorage.getItem(key));
                    drafts.push(draft);
                } catch (e) {
                    console.error('Error loading draft:', e);
                }
            }
        }
        return drafts.sort((a, b) => b.timestamp - a.timestamp);
    }
    
    // Keyboard shortcuts
    setupKeyboardShortcuts() {
        document.addEventListener('keydown', (e) => {
            if (e.ctrlKey || e.metaKey) {
                switch (e.key) {
                    case 's':
                        e.preventDefault();
                        this.saveToDraft();
                        break;
                    case 'Enter':
                        e.preventDefault();
                        this.generatePaper();
                        break;
                    case 'n':
                        e.preventDefault();
                        window.location.href = '/generate';
                        break;
                }
            }
        });
    }
    
    // Real-time preview
    setupRealTimePreview() {
        const topicInput = document.getElementById('topic');
        if (topicInput) {
            let debounceTimer;
            topicInput.addEventListener('input', (e) => {
                clearTimeout(debounceTimer);
                debounceTimer = setTimeout(() => {
                    this.showPreview(e.target.value);
                }, 500);
            });
        }
    }
    
    async showPreview(topic) {
        if (!topic || topic.length < 5) return;
        
        const previewContainer = document.getElementById('topicPreview');
        if (!previewContainer) return;
        
        previewContainer.innerHTML = `
            <div class="card mt-3">
                <div class="card-header">
                    <h6 class="mb-0">Topic Preview</h6>
                </div>
                <div class="card-body">
                    <div class="d-flex align-items-center">
                        <div class="spinner-border spinner-border-sm me-2" role="status"></div>
                        <span>Analyzing topic...</span>
                    </div>
                </div>
            </div>
        `;
        
        try {
            const response = await fetch('/api/analyze-topic', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic })
            });
            
            const data = await response.json();
            
            previewContainer.innerHTML = `
                <div class="card mt-3">
                    <div class="card-header">
                        <h6 class="mb-0">Topic Analysis</h6>
                    </div>
                    <div class="card-body">
                        <p><strong>Scope:</strong> ${data.scope || 'Good scope for research'}</p>
                        <p><strong>Suggested Sections:</strong></p>
                        <ul class="mb-0">
                            ${(data.sections || ['Introduction', 'Literature Review', 'Methodology', 'Results', 'Conclusion']).map(section => `<li>${section}</li>`).join('')}
                        </ul>
                    </div>
                </div>
            `;
        } catch (error) {
            previewContainer.innerHTML = '';
        }
    }
    
    // Utility methods
    generateId() {
        return Date.now().toString(36) + Math.random().toString(36).substr(2);
    }
    
    showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `alert alert-${type} notification animate__animated animate__fadeInRight`;
        notification.innerHTML = `
            ${message}
            <button type="button" class="btn-close" onclick="this.parentElement.remove()"></button>
        `;
        notification.style.position = 'fixed';
        notification.style.top = '20px';
        notification.style.right = '20px';
        notification.style.zIndex = '9999';
        notification.style.minWidth = '300px';
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.classList.add('animate__fadeOutRight');
            setTimeout(() => notification.remove(), 500);
        }, 4000);
    }
}

// Initialize
const paperGenerator = new PaperGenerator();

// Global functions for HTML onclick events
window.selectTemplate = (templateId) => {
    document.getElementById('paperType').value = templateId;
    document.querySelectorAll('.template-card').forEach(card => {
        card.classList.remove('selected');
    });
    event.target.closest('.template-card').classList.add('selected');
};

// Enhanced form validation
class FormValidator {
    static validatePaperForm(formData) {
        const errors = [];
        
        if (!formData.topic || formData.topic.trim().length < 5) {
            errors.push('Topic must be at least 5 characters long');
        }
        
        if (formData.topic && formData.topic.length > 200) {
            errors.push('Topic must be less than 200 characters');
        }
        
        const validTypes = ['research', 'review', 'essay', 'thesis', 'report'];
        if (!validTypes.includes(formData.paper_type)) {
            errors.push('Invalid paper type selected');
        }
        
        return errors;
    }
    
    static showValidationErrors(errors) {
        const errorContainer = document.getElementById('validationErrors');
        if (!errorContainer) return;
        
        if (errors.length === 0) {
            errorContainer.style.display = 'none';
            return;
        }
        
        errorContainer.innerHTML = `
            <div class="alert alert-danger">
                <h6>Please fix the following errors:</h6>
                <ul class="mb-0">
                    ${errors.map(error => `<li>${error}</li>`).join('')}
                </ul>
            </div>
        `;
        errorContainer.style.display = 'block';
    }
}

// Export functionality
class ExportManager {
    static async exportToPDF(content, title) {
        // This would integrate with a PDF generation service
        showAlert('PDF export coming soon! Use LaTeX for now.', 'info');
    }
    
    static async exportToWord(content, title) {
        // This would integrate with a Word document generation service
        showAlert('Word export coming soon! Copy text for now.', 'info');
    }
    
    static exportToMarkdown(content, title) {
        const markdownContent = `# ${title}\n\n${content}`;
        const blob = new Blob([markdownContent], { type: 'text/markdown' });
        this.downloadFile(blob, `${title}.md`);
    }
    
    static downloadFile(blob, filename) {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
    }
}

// Real-time collaboration features
class CollaborationManager {
    constructor() {
        this.sessionId = this.generateSessionId();
        this.collaborators = [];
    }
    
    generateSessionId() {
        return 'session_' + Math.random().toString(36).substr(2, 9);
    }
    
    shareSession() {
        const shareUrl = `${window.location.origin}/collaborate/${this.sessionId}`;
        navigator.clipboard.writeText(shareUrl).then(() => {
            showAlert('Collaboration link copied to clipboard!', 'success');
        });
    }
    
    // This would integrate with WebSocket for real-time collaboration
    setupRealtimeSync() {
        // WebSocket implementation would go here
    }
}

// Performance monitoring
class PerformanceMonitor {
    static trackGeneration(startTime, endTime, wordCount) {
        const duration = endTime - startTime;
        const wordsPerSecond = Math.round(wordCount / (duration / 1000));
        
        console.log(`Generation completed in ${duration}ms`);
        console.log(`Performance: ${wordsPerSecond} words/second`);
        
        // Send analytics (in a real app)
        this.sendAnalytics('paper_generated', {
            duration,
            wordCount,
            wordsPerSecond
        });
    }
    
    static sendAnalytics(event, data) {
        // Analytics implementation would go here
        console.log('Analytics:', event, data);
    }
}
