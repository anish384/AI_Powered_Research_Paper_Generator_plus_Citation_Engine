import re
import json
from collections import Counter
from datetime import datetime

class AnalyticsService:
    def __init__(self):
        pass
    
    def analyze_readability(self, content):
        """Analyze content readability and complexity"""
        sentences = re.split(r'[.!?]+', content)
        words = content.split()
        
        # Basic metrics
        word_count = len(words)
        sentence_count = len([s for s in sentences if s.strip()])
        avg_words_per_sentence = word_count / max(sentence_count, 1)
        
        # Complex word analysis
        complex_words = [w for w in words if len(w) > 6]
        complex_word_ratio = len(complex_words) / max(word_count, 1)
        
        # Academic vocabulary analysis
        academic_indicators = ['however', 'furthermore', 'consequently', 'nevertheless', 'therefore', 'moreover']
        academic_score = sum(1 for word in words if word.lower() in academic_indicators)
        
        return {
            'word_count': word_count,
            'sentence_count': sentence_count,
            'avg_words_per_sentence': round(avg_words_per_sentence, 2),
            'complex_word_ratio': round(complex_word_ratio, 3),
            'academic_score': academic_score,
            'readability_level': self._calculate_readability_level(avg_words_per_sentence, complex_word_ratio)
        }
    
    def _calculate_readability_level(self, avg_words, complex_ratio):
        """Calculate readability level"""
        if avg_words > 20 and complex_ratio > 0.3:
            return "Graduate"
        elif avg_words > 15 and complex_ratio > 0.2:
            return "Undergraduate"
        elif avg_words > 12:
            return "High School"
        else:
            return "General Public"
    
    def analyze_argument_structure(self, content):
        """Analyze argument structure and flow"""
        # Identify argument indicators
        claim_indicators = ['argue', 'claim', 'assert', 'propose', 'suggest']
        evidence_indicators = ['evidence', 'data', 'research', 'study', 'findings']
        transition_indicators = ['however', 'furthermore', 'in contrast', 'similarly', 'therefore']
        
        claims = sum(1 for word in content.lower().split() if word in claim_indicators)
        evidence = sum(1 for word in content.lower().split() if word in evidence_indicators)
        transitions = sum(1 for word in content.lower().split() if word in transition_indicators)
        
        return {
            'claim_density': claims,
            'evidence_density': evidence,
            'transition_density': transitions,
            'argument_balance': round(evidence / max(claims, 1), 2),
            'flow_score': transitions
        }
    
    def generate_improvement_suggestions(self, content):
        """Generate specific improvement suggestions"""
        readability = self.analyze_readability(content)
        argument = self.analyze_argument_structure(content)
        
        suggestions = []
        
        # Readability suggestions
        if readability['avg_words_per_sentence'] > 25:
            suggestions.append("Consider breaking down long sentences for better readability")
        
        if readability['complex_word_ratio'] > 0.4:
            suggestions.append("Balance complex terminology with clearer explanations")
        
        # Argument structure suggestions
        if argument['argument_balance'] < 0.5:
            suggestions.append("Strengthen arguments with more evidence and supporting data")
        
        if argument['flow_score'] < 5:
            suggestions.append("Add more transitional phrases to improve logical flow")
        
        return suggestions
    
    def generate_quality_score(self, content):
        """Generate overall quality score"""
        readability = self.analyze_readability(content)
        argument = self.analyze_argument_structure(content)
        
        # Scoring algorithm
        readability_score = min(100, (readability['academic_score'] * 5) + 50)
        argument_score = min(100, (argument['argument_balance'] * 30) + (argument['flow_score'] * 5))
        
        overall_score = (readability_score + argument_score) / 2
        
        return {
            'overall_score': round(overall_score, 1),
            'readability_score': round(readability_score, 1),
            'argument_score': round(argument_score, 1),
            'grade': self._get_grade(overall_score)
        }
    
    def _get_grade(self, score):
        """Convert score to letter grade"""
        if score >= 90: return 'A'
        elif score >= 80: return 'B'
        elif score >= 70: return 'C'
        elif score >= 60: return 'D'
        else: return 'F'