<!DOCTYPE html>
<html lang="zh-CN" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OpenClash Config Builder - 自动化覆写配置生成器</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'system-ui', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                    },
                    colors: {
                        primary: '#3b82f6',
                        secondary: '#6366f1',
                        accent: '#06b6d4',
                        dark: '#0f172a',
                        'dark-light': '#1e293b',
                    },
                    animation: {
                        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
                        'float': 'float 6s ease-in-out infinite',
                        'slide-up': 'slideUp 0.5s ease-out',
                    },
                    keyframes: {
                        float: {
                            '0%, 100%': { transform: 'translateY(0)' },
                            '50%': { transform: 'translateY(-10px)' },
                        },
                        slideUp: {
                            '0%': { transform: 'translateY(20px)', opacity: '0' },
                            '100%': { transform: 'translateY(0)', opacity: '1' },
                        }
                    }
                }
            }
        }
    </script>
    <style>
        .glass {
            background: rgba(30, 41, 59, 0.7);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .gradient-text {
            background: linear-gradient(135deg, #3b82f6 0%, #06b6d4 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .code-block {
            background: #1e293b;
            border-radius: 0.5rem;
            position: relative;
            overflow: hidden;
        }
        .code-block::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, #3b82f6, #06b6d4);
        }
        .tree-line {
            border-left: 2px solid #334155;
            padding-left: 1.5rem;
            margin-left: 0.5rem;
        }
        .feature-card {
            transition: all 0.3s ease;
        }
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.3);
        }
    </style>
</head>
<body class="bg-dark text-gray-100 font-sans antialiased selection:bg-primary selection:text-white">

    <!-- Hero Section -->
    <header class="relative min-h-screen flex items-center justify-center overflow-hidden">
        <div class="absolute inset-0 bg-gradient-to-br from-dark via-dark-light to-dark opacity-90"></div>
        <div class="absolute inset-0">
            <div class="absolute top-20 left-10 w-72 h-72 bg-primary/20 rounded-full blur-3xl animate-pulse-slow"></div>
            <div class="absolute bottom-20 right-10 w-96 h-96 bg-secondary/20 rounded-full blur-3xl animate-pulse-slow" style="animation-delay: 1s;"></div>
        </div>

        <div class="relative z-10 container mx-auto px-6 text-center">
            <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/5 border border-white/10 mb-8 animate-slide-up">
                <span class="w-2 h-2 rounded-full bg-green-400 animate-pulse"></span>
                <span class="text-sm text-gray-400">自动化构建系统运行中</span>
            </div>

            <h1 class="text-5xl md:text-7xl font-bold mb-6 animate-slide-up" style="animation-delay: 0.1s;">
                <span class="gradient-text">OpenClash</span><br>
                <span class="text-white">Config Builder</span>
            </h1>

            <p class="text-xl md:text-2xl text-gray-400 max-w-2xl mx-auto mb-12 animate-slide-up" style="animation-delay: 0.2s;">
                智能提取 · 自动精简 · 动态生成<br>
                <span class="text-sm md:text-base text-gray-500 mt-2 block">从上游 YAML 到 OpenClash 覆写配置的一站式解决方案</span>
            </p>

            <div class="flex flex-col md:flex-row gap-4 justify-center items-center animate-slide-up" style="animation-delay: 0.3s;">
                <a href="#quick-start" class="px-8 py-4 bg-primary hover:bg-blue-600 text-white rounded-lg font-semibold transition-all flex items-center gap-2 group">
                    <i class="fas fa-rocket group-hover:translate-x-1 transition-transform"></i>
                    快速开始
                </a>
                <a href="https://github.com/YOUR_USERNAME/YOUR_REPO" target="_blank" class="px-8 py-4 glass hover:bg-white/10 text-white rounded-lg font-semibold transition-all flex items-center gap-2">
                    <i class="fab fa-github"></i>
                    查看源码
                </a>
            </div>

            <div class="mt-16 flex justify-center gap-6 text-gray-500 animate-slide-up" style="animation-delay: 0.4s;">
                <div class="flex items-center gap-2">
                    <i class="fas fa-sync-alt text-primary"></i>
                    <span>每日自动同步</span>
                </div>
                <div class="flex items-center gap-2">
                    <i class="fas fa-code-branch text-secondary"></i>
                    <span>动态变量生成</span>
                </div>
                <div class="flex items-center gap-2">
                    <i class="fas fa-bolt text-accent"></i>
                    <span>零配置部署</span>
                </div>
            </div>
        </div>

        <div class="absolute bottom-10 left-1/2 -translate-x-1/2 animate-bounce">
            <i class="fas fa-chevron-down text-gray-600 text-2xl"></i>
        </div>
    </header>

    <!-- Features Grid -->
    <section class="py-20 bg-dark-light/30">
        <div class="container mx-auto px-6">
            <div class="text-center mb-16">
                <h2 class="text-3xl md:text-4xl font-bold mb-4">核心特性</h2>
                <p class="text-gray-400">全自动化的配置管理流水线</p>
            </div>

            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                <div class="feature-card glass p-6 rounded-xl">
                    <div class="w-12 h-12 bg-blue-500/20 rounded-lg flex items-center justify-center mb-4 text-blue-400">
                        <i class="fas fa-sync-alt text-2xl"></i>
                    </div>
                    <h3 class="text-xl font-semibold mb-2">自动同步上游</h3>
                    <p class="text-gray-400 text-sm">每日定时从 HenryChiao/mihomo_yamls 拉取最新配置，保持规则集始终更新</p>
                </div>

                <div class="feature-card glass p-6 rounded-xl">
                    <div class="w-12 h-12 bg-purple-500/20 rounded-lg flex items-center justify-center mb-4 text-purple-400">
                        <i class="fas fa-cut text-2xl"></i>
                    </div>
                    <h3 class="text-xl font-semibold mb-2">智能精简</h3>
                    <p class="text-gray-400 text-sm">自动删除 port、dns、tun 等 OpenClash 管理字段，仅保留核心代理和规则配置</p>
                </div>

                <div class="feature-card glass p-6 rounded-xl">
                    <div class="w-12 h-12 bg-cyan-500/20 rounded-lg flex items-center justify-center mb-4 text-cyan-400">
                        <i class="fas fa-variable text-2xl"></i>
                    </div>
                    <h3 class="text-xl font-semibold mb-2">动态变量生成</h3>
                    <p class="text-gray-400 text-sm">根据 proxy-provider 数量自动识别并生成 EN_KEY / EN_KEY1...N 环境变量要求</p>
                </div>

                <div class="feature-card glass p-6 rounded-xl">
                    <div class="w-12 h-12 bg-green-500/20 rounded-lg flex items-center justify-center mb-4 text-green-400">
                        <i class="fas fa-network-wired text-2xl"></i>
                    </div>
                    <h3 class="text-xl font-semibold mb-2">三模式支持</h3>
                    <p class="text-gray-400 text-sm">自动生成主路由、旁路由(+EN_DNS)、Smart 智能模式三种覆写配置</p>
                </div>

                <div class="feature-card glass p-6 rounded-xl">
                    <div class="w-12 h-12 bg-orange-500/20 rounded-lg flex items-center justify-center mb-4 text-orange-400">
                        <i class="fas fa-code text-2xl"></i>
                    </div>
                    <h3 class="text-xl font-semibold mb-2">本地配置支持</h3>
                    <p class="text-gray-400 text-sm">通过 cleaner_config/ 目录维护自定义配置，与外部配置一起处理</p>
                </div>

                <div class="feature-card glass p-6 rounded-xl">
                    <div class="w-12 h-12 bg-pink-500/20 rounded-lg flex items-center justify-center mb-4 text-pink-400">
                        <i class="fas fa-robot text-2xl"></i>
                    </div>
                    <h3 class="text-xl font-semibold mb-2">零人工干预</h3>
                    <p class="text-gray-400 text-sm">GitHub Actions 全自动构建，直接提交到仓库 overwrite/ 目录，可直接编辑</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Workflow Visualization -->
    <section class="py-20">
        <div class="container mx-auto px-6">
            <div class="text-center mb-16">
                <h2 class="text-3xl md:text-4xl font-bold mb-4">工作流程</h2>
                <p class="text-gray-400">从上游到成品的全自动化流程</p>
            </div>

            <div class="relative max-w-4xl mx-auto">
                <div class="absolute left-1/2 top-0 bottom-0 w-1 bg-gradient-to-b from-blue-500 to-cyan-500 -translate-x-1/2 hidden md:block"></div>

                <div class="space-y-12">
                    <div class="relative flex flex-col md:flex-row items-center gap-8">
                        <div class="flex-1 text-right hidden md:block">
                            <h3 class="text-xl font-semibold text-blue-400">1. 同步上游</h3>
                            <p class="text-gray-400 mt-2">从 HenryChiao/mihomo_yamls 克隆 THEYAMLS 目录下的 General_Config 和 Smart_Mode</p>
                        </div>
                        <div class="w-16 h-16 rounded-full bg-dark-light border-2 border-blue-500 flex items-center justify-center z-10 shadow-lg shadow-blue-500/20">
                            <i class="fas fa-download text-blue-400 text-xl"></i>
                        </div>
                        <div class="flex-1 md:hidden text-center">
                            <h3 class="text-xl font-semibold text-blue-400">1. 同步上游</h3>
                            <p class="text-gray-400 mt-2">获取最新 YAML 配置</p>
                        </div>
                        <div class="flex-1 hidden md:block"></div>
                    </div>

                    <div class="relative flex flex-col md:flex-row items-center gap-8">
                        <div class="flex-1 hidden md:block"></div>
                        <div class="w-16 h-16 rounded-full bg-dark-light border-2 border-purple-500 flex items-center justify-center z-10 shadow-lg shadow-purple-500/20">
                            <i class="fas fa-filter text-purple-400 text-xl"></i>
                        </div>
                        <div class="flex-1 text-center md:text-left">
                            <h3 class="text-xl font-semibold text-purple-400">2. 精简处理</h3>
                            <p class="text-gray-400 mt-2">提取 proxy-providers, proxy-groups, rule-providers, rules 及锚点定义，删除 OpenClash 管理字段</p>
                        </div>
                    </div>

                    <div class="relative flex flex-col md:flex-row items-center gap-8">
                        <div class="flex-1 text-right hidden md:block">
                            <h3 class="text-xl font-semibold text-cyan-400">3. 分析生成</h3>
                            <p class="text-gray-400 mt-2">统计 Provider 数量，生成对应环境变量，渲染 Jinja2 模板</p>
                        </div>
                        <div class="w-16 h-16 rounded-full bg-dark-light border-2 border-cyan-500 flex items-center justify-center z-10 shadow-lg shadow-cyan-500/20">
                            <i class="fas fa-cogs text-cyan-400 text-xl"></i>
                        </div>
                        <div class="flex-1 md:hidden text-center">
                            <h3 class="text-xl font-semibold text-cyan-400">3. 分析生成</h3>
                            <p class="text-gray-400 mt-2">生成 .conf 覆写文件</p>
                        </div>
                        <div class="flex-1 hidden md:block"></div>
                    </div>

                    <div class="relative flex flex-col md:flex-row items-center gap-8">
                        <div class="flex-1 hidden md:block"></div>
                        <div class="w-16 h-16 rounded-full bg-dark-light border-2 border-green-500 flex items-center justify-center z-10 shadow-lg shadow-green-500/20">
                            <i class="fas fa-save text-green-400 text-xl"></i>
                        </div>
                        <div class="flex-1 text-center md:text-left">
                            <h3 class="text-xl font-semibold text-green-400">4. 提交仓库</h3>
                            <p class="text-gray-400 mt-2">自动提交到 overwrite/ 和 processed_configs/ 目录，可直接浏览和编辑</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Directory Structure -->
    <section class="py-20 bg-dark-light/30">
        <div class="container mx-auto px-6">
            <div class="grid lg:grid-cols-2 gap-12 items-start">
                <div>
                    <h2 class="text-3xl font-bold mb-6">项目结构</h2>
                    <p class="text-gray-400 mb-8">清晰的目录划分，自动化与手动配置分离</p>
                    
                    <div class="glass rounded-xl p-6 font-mono text-sm">
                        <div class="text-gray-400 mb-2">your-repo/</div>
                        <div class="tree-line space-y-1">
                            <div class="flex items-center gap-2 text-yellow-400">
                                <i class="fas fa-folder"></i>
                                <span>.github/workflows/</span>
                                <span class="text-gray-500 text-xs">CI配置</span>
                            </div>
                            <div class="flex items-center gap-2 text-blue-400">
                                <i class="fas fa-folder"></i>
                                <span>src/</span>
                                <span class="text-gray-500 text-xs">Python脚本</span>
                            </div>
                            <div class="pl-8 space-y-1 text-gray-300">
                                <div><i class="fab fa-python text-blue-300 mr-2"></i>yaml_processor.py</div>
                                <div><i class="fab fa-python text-blue-300 mr-2"></i>overwrite_generator.py</div>
                            </div>
                            <div class="flex items-center gap-2 text-purple-400">
                                <i class="fas fa-folder"></i>
                                <span>templates/</span>
                                <span class="text-gray-500 text-xs">Jinja2模板</span>
                            </div>
                            <div class="pl-8 space-y-1 text-gray-300">
                                <div><i class="fas fa-file-code text-gray-400 mr-2"></i>main.conf.j2</div>
                                <div><i class="fas fa-file-code text-gray-400 mr-2"></i>bypass.conf.j2</div>
                                <div><i class="fas fa-file-code text-gray-400 mr-2"></i>smart.conf.j2</div>
                            </div>
                            <div class="flex items-center gap-2 text-green-400">
                                <i class="fas fa-folder"></i>
                                <span>cleaner_config/</span>
                                <span class="text-gray-500 text-xs">本地配置源</span>
                            </div>
                            <div class="flex items-center gap-2 text-orange-400">
                                <i class="fas fa-folder"></i>
                                <span>processed_configs/</span>
                                <span class="text-gray-500 text-xs">精简后的YAML</span>
                            </div>
                            <div class="pl-8 flex items-center gap-2 text-gray-300">
                                <i class="fas fa-folder text-yellow-600"></i>
                                <span>external/</span>
                            </div>
                            <div class="pl-8 flex items-center gap-2 text-gray-300">
                                <i class="fas fa-folder text-yellow-600"></i>
                                <span>local/</span>
                            </div>
                            <div class="flex items-center gap-2 text-pink-400 font-semibold">
                                <i class="fas fa-folder-open"></i>
                                <span>overwrite/</span>
                                <span class="text-gray-500 text-xs font-normal">生成的覆写文件</span>
                            </div>
                            <div class="pl-8 space-y-1 text-gray-300 text-xs">
                                <div><i class="fas fa-file-alt text-gray-400 mr-2"></i>Overwrite-external-*.conf</div>
                                <div><i class="fas fa-file-alt text-gray-400 mr-2"></i>Overwrite-local-*.conf</div>
                                <div><i class="fas fa-info-circle text-blue-400 mr-2"></i>README.md</div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="space-y-6">
                    <div class="glass rounded-xl p-6 border-l-4 border-blue-500">
                        <h4 class="font-semibold text-lg mb-2 flex items-center gap-2">
                            <i class="fas fa-code text-blue-400"></i>
                            外部配置 (External)
                        </h4>
                        <p class="text-gray-400 text-sm">自动从 HenryChiao/mihomo_yamls 同步，存放于 processed_configs/external/，每日更新</p>
                    </div>

                    <div class="glass rounded-xl p-6 border-l-4 border-green-500">
                        <h4 class="font-semibold text-lg mb-2 flex items-center gap-2">
                            <i class="fas fa-home text-green-400"></i>
                            本地配置 (Local)
                        </h4>
                        <p class="text-gray-400 text-sm">通过 cleaner_config/ 目录维护，适合自定义规则或私有配置，与外部配置隔离</p>
                    </div>

                    <div class="glass rounded-xl p-6 border-l-4 border-pink-500">
                        <h4 class="font-semibold text-lg mb-2 flex items-center gap-2">
                            <i class="fas fa-magic text-pink-400"></i>
                            覆写文件 (Overwrite)
                        </h4>
                        <p class="text-gray-400 text-sm">最终生成的 .conf 文件，按 主路由/旁路由/Smart 三种模式分别生成，可直接在 GitHub 上编辑</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Usage Guide -->
    <section id="quick-start" class="py-20">
        <div class="container mx-auto px-6 max-w-4xl">
            <div class="text-center mb-12">
                <h2 class="text-3xl font-bold mb-4">使用方法</h2>
                <p class="text-gray-400">三步完成覆写配置部署</p>
            </div>

            <div class="space-y-8">
                <div class="glass rounded-xl p-8 relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-blue-500/10 rounded-full -mr-16 -mt-16"></div>
                    <div class="relative z-10">
                        <div class="flex items-center gap-4 mb-4">
                            <div class="w-10 h-10 rounded-full bg-blue-500 flex items-center justify-center font-bold text-lg">1</div>
                            <h3 class="text-xl font-semibold">选择配置文件</h3>
                        </div>
                        <p class="text-gray-400 mb-4">进入仓库的 <code class="bg-dark-light px-2 py-1 rounded text-blue-400">overwrite/</code> 目录，根据文件名选择适合的配置：</p>
                        <div class="grid md:grid-cols-3 gap-4 text-sm">
                            <div class="bg-dark-light/50 p-4 rounded-lg border border-gray-700">
                                <div class="font-semibold text-blue-400 mb-2">主路由模式</div>
                                <div class="text-gray-500 text-xs">Overwrite-*-main.conf</div>
                                <div class="mt-2 text-gray-400">标准 Url-test 模式，适合作为主路由</div>
                            </div>
                            <div class="bg-dark-light/50 p-4 rounded-lg border border-gray-700">
                                <div class="font-semibold text-orange-400 mb-2">旁路由模式</div>
                                <div class="text-gray-500 text-xs">Overwrite-*-bypass.conf</div>
                                <div class="mt-2 text-gray-400">需额外设置 EN_DNS，适合旁路由</div>
                            </div>
                            <div class="bg-dark-light/50 p-4 rounded-lg border border-gray-700">
                                <div class="font-semibold text-purple-400 mb-2">Smart 模式</div>
                                <div class="text-gray-500 text-xs">Overwrite-*-smart.conf</div>
                                <div class="mt-2 text-gray-400">自动选择最优节点，支持模型训练</div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="glass rounded-xl p-8 relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-green-500/10 rounded-full -mr-16 -mt-16"></div>
                    <div class="relative z-10">
                        <div class="flex items-center gap-4 mb-4">
                            <div class="w-10 h-10 rounded-full bg-green-500 flex items-center justify-center font-bold text-lg">2</div>
                            <h3 class="text-xl font-semibold">配置环境变量</h3>
                        </div>
                        <p class="text-gray-400 mb-4">根据生成的覆写文件中的 provider 数量，在 OpenClash 中设置对应的环境变量：</p>
                        
                        <div class="space-y-4">
                            <div class="code-block p-4 font-mono text-sm">
                                <div class="flex items-center justify-between mb-2 text-xs text-gray-500 border-b border-gray-700 pb-2">
                                    <span>单 Provider 配置</span>
                                    <span class="text-green-400">1 个订阅</span>
                                </div>
                                <div class="text-gray-300">
                                    EN_KEY=<span class="text-green-400">https://your-subscription-url</span>
                                </div>
                            </div>

                            <div class="code-block p-4 font-mono text-sm">
                                <div class="flex items-center justify-between mb-2 text-xs text-gray-500 border-b border-gray-700 pb-2">
                                    <span>多 Provider 配置</span>
                                    <span class="text-blue-400">2+ 个订阅</span>
                                </div>
                                <div class="text-gray-300 space-y-1">
                                    <div>EN_KEY1=<span class="text-green-400">https://sub1-url</span></div>
                                    <div>EN_KEY2=<span class="text-green-400">https://sub2-url</span></div>
                                    <div>EN_KEY3=<span class="text-green-400">https://sub3-url</span></div>
                                </div>
                            </div>

                            <div class="code-block p-4 font-mono text-sm border border-orange-500/30">
                                <div class="flex items-center justify-between mb-2 text-xs text-gray-500 border-b border-gray-700 pb-2">
                                    <span>旁路由额外变量</span>
                                    <span class="text-orange-400">必需</span>
                                </div>
                                <div class="text-gray-300">
                                    EN_DNS=<span class="text-orange-400">223.5.5.5,114.114.114.114</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="glass rounded-xl p-8 relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-purple-500/10 rounded-full -mr-16 -mt-16"></div>
                    <div class="relative z-10">
                        <div class="flex items-center gap-4 mb-4">
                            <div class="w-10 h-10 rounded-full bg-purple-500 flex items-center justify-center font-bold text-lg">3</div>
                            <h3 class="text-xl font-semibold">应用覆写</h3>
                        </div>
                        <ol class="list-decimal list-inside space-y-2 text-gray-400">
                            <li>在 OpenClash 的<strong>覆写设置</strong>中上传 .conf 文件</li>
                            <li>或订阅 <code class="bg-dark-light px-2 py-0.5 rounded text-xs">overwrite/xxx.conf</code> 的 Raw URL</li>
                            <li>在<strong>全局设置</strong>中填入上述环境变量</li>
                            <li>保存并重启 OpenClash</li>
                        </ol>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Naming Convention -->
    <section class="py-20 bg-dark-light/30">
        <div class="container mx-auto px-6">
            <h2 class="text-3xl font-bold text-center mb-12">文件命名规则</h2>
            
            <div class="max-w-4xl mx-auto overflow-x-auto">
                <table class="w-full text-left border-collapse">
                    <thead>
                        <tr class="border-b border-gray-700">
                            <th class="pb-4 text-gray-400 font-semibold">文件名模式</th>
                            <th class="pb-4 text-gray-400 font-semibold">来源</th>
                            <th class="pb-4 text-gray-400 font-semibold">模式</th>
                            <th class="pb-4 text-gray-400 font-semibold">Provider变量</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-gray-800">
                        <tr class="group hover:bg-white/5 transition-colors">
                            <td class="py-4 font-mono text-sm text-blue-400">Overwrite-external-xxx-main.conf</td>
                            <td class="py-4 text-gray-300">HenryChiao 仓库</td>
                            <td class="py-4"><span class="px-2 py-1 bg-blue-500/20 text-blue-400 rounded text-xs">主路由</span></td>
                            <td class="py-4 font-mono text-sm text-gray-400">EN_KEY / EN_KEY1-N</td>
                        </tr>
                        <tr class="group hover:bg-white/5 transition-colors">
                            <td class="py-4 font-mono text-sm text-orange-400">Overwrite-external-xxx-bypass.conf</td>
                            <td class="py-4 text-gray-300">HenryChiao 仓库</td>
                            <td class="py-4"><span class="px-2 py-1 bg-orange-500/20 text-orange-400 rounded text-xs">旁路由</span></td>
                            <td class="py-4 font-mono text-sm text-gray-400">EN_KEY+EN_DNS</td>
                        </tr>
                        <tr class="group hover:bg-white/5 transition-colors">
                            <td class="py-4 font-mono text-sm text-purple-400">Overwrite-external-xxx-smart.conf</td>
                            <td class="py-4 text-gray-300">HenryChiao 仓库</td>
                            <td class="py-4"><span class="px-2 py-1 bg-purple-500/20 text-purple-400 rounded text-xs">Smart</span></td>
                            <td class="py-4 font-mono text-sm text-gray-400">EN_KEY / EN_KEY1-N</td>
                        </tr>
                        <tr class="group hover:bg-white/5 transition-colors">
                            <td class="py-4 font-mono text-sm text-green-400">Overwrite-local-xxx-main.conf</td>
                            <td class="py-4 text-gray-300">cleaner_config/</td>
                            <td class="py-4"><span class="px-2 py-1 bg-blue-500/20 text-blue-400 rounded text-xs">主路由</span></td>
                            <td class="py-4 font-mono text-sm text-gray-400">视配置而定</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="py-12 border-t border-gray-800">
        <div class="container mx-auto px-6 text-center">
            <div class="flex justify-center gap-6 mb-8">
                <a href="https://github.com/vernesong/OpenClash" target="_blank" class="text-gray-400 hover:text-white transition-colors">
                    <i class="fas fa-external-link-alt mr-2"></i>OpenClash
                </a>
                <a href="https://github.com/HenryChiao/mihomo_yamls" target="_blank" class="text-gray-400 hover:text-white transition-colors">
                    <i class="fas fa-external-link-alt mr-2"></i>mihomo_yamls
                </a>
                <a href="https://wiki.metacubex.one/" target="_blank" class="text-gray-400 hover:text-white transition-colors">
                    <i class="fas fa-book mr-2"></i>Mihomo Wiki
                </a>
            </div>
            <p class="text-gray-600 text-sm">
                基于 GPL-3.0 许可证开源 · 使用 GitHub Actions 自动构建
            </p>
        </div>
    </footer>

    <script>
        // Smooth scroll for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });

        // Add scroll animation observer
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-slide-up');
                    entry.target.style.opacity = '1';
                }
            });
        }, observerOptions);

        document.querySelectorAll('.glass, .feature-card').forEach((el) => {
            el.style.opacity = '0';
            observer.observe(el);
        });
    </script>
</body>
</html>
