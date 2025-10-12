/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter var', 'Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'Fira Code', 'ui-monospace', 'SFMono-Regular', 'monospace'],
      },
      colors: {
        warm: {
          50: '#fdfcfb',
          100: '#faf8f5',
          200: '#f4f0ea',
          300: '#ebe4db',
          400: '#ddd4c7',
          500: '#cbc0af',
          600: '#b5a693',
          700: '#9a8b75',
          800: '#7c6f5d',
          900: '#645a4b',
        },
        stone: {
          50: '#fafaf9',
          100: '#f5f5f4',
          200: '#e7e5e4',
          300: '#d6d3d1',
          400: '#a8a29e',
          500: '#78716c',
          600: '#57534e',
          700: '#44403c',
          800: '#292524',
          900: '#1c1917',
        },
        amber: {
          50: '#fffbeb',
          100: '#fef3c7',
          200: '#fde68a',
          300: '#fcd34d',
          400: '#fbbf24',
          500: '#f59e0b',
          600: '#d97706',
          700: '#b45309',
          800: '#92400e',
          900: '#78350f',
        }
      },
      lineHeight: {
        'relaxed-reading': '1.75',
        'tight-heading': '1.15',
      },
      letterSpacing: {
        'slight': '0.015em',
      },
      typography: {
        DEFAULT: {
          css: {
            color: '#44403c',
            lineHeight: '1.75',
            fontSize: '1.125rem',
            a: {
              color: '#f59e0b',
              textDecoration: 'none',
              fontWeight: '500',
              '&:hover': {
                color: '#d97706',
              },
            },
            strong: {
              color: '#1c1917',
              fontWeight: '600',
            },
            code: {
              backgroundColor: '#faf8f5',
              color: '#44403c',
              padding: '0.25rem 0.5rem',
              borderRadius: '0.375rem',
              fontWeight: '500',
              fontSize: '0.875rem',
            },
            'code::before': {
              content: '""',
            },
            'code::after': {
              content: '""',
            },
            pre: {
              backgroundColor: '#fdfcfb',
              border: '1px solid #e7e5e4',
              borderRadius: '0.5rem',
              padding: '1.5rem',
              fontSize: '0.875rem',
              lineHeight: '1.6',
            },
            blockquote: {
              borderLeftColor: '#f59e0b',
              borderLeftWidth: '4px',
              paddingLeft: '1.5rem',
              fontStyle: 'italic',
              color: '#78716c',
            },
            h1: {
              fontSize: '2.25rem',
              fontWeight: '300',
              lineHeight: '1.15',
              letterSpacing: '0.015em',
              color: '#1c1917',
            },
            h2: {
              fontSize: '1.875rem',
              fontWeight: '400',
              lineHeight: '1.2',
              color: '#1c1917',
              marginTop: '2.5rem',
              marginBottom: '1.5rem',
            },
            h3: {
              fontSize: '1.5rem',
              fontWeight: '500',
              lineHeight: '1.25',
              color: '#1c1917',
              marginTop: '2rem',
              marginBottom: '1rem',
            },
            p: {
              marginTop: '1.25rem',
              marginBottom: '1.25rem',
            },
          },
        },
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
