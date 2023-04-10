from dash import html
import dash_bootstrap_components as dbc

head_dominador = 'Dominador'
body_dominador = 'As pessoas com o estilo Dominante são diretas e decididas. Assumem confortavelmente posições de liderança e lidam bem com situações de conflito e pressão. São autoconfiantes, audaciosas, competitivas e gostam de desafios. Trabalham geralmente com o foco nos resultados e objetivos a serem atingidos e estão acostumadas a agir de maneira mais ativa e enérgica.'
head_influenciador = 'Influenciador'
body_influenciador ='As pessoas com o estilo influente são faladoras, extrovertidas, amigáveis e disponíveis para os outros. Necessitam de estar com outras pessoas e desenvolver relacionamentos. Adoram expressar suas ideias e quase nunca lhe faltam assuntos para conversar. São geralmente otimistas, alegres, entusiasmadas e, por isso, possuem facilidade para motivar e influenciar as pessoas ao seu redor.Trabalham melhor em equipe e costumam manter os ambientes positivos com seu entusiasmo e senso de humor, o que acaba  contagiando as pessoas ao seu redor. Vaidosos, estão sempre buscando reconhecimento social e normalmente valorizam status e prestígio, pois não gostam de passar despercebidos. Envolvem-se, portanto, em oportunidades sociais para desenvolver relacionamentos, tais como viagens, festas e outros entretenimentos em grupo. Raramente se entediam e gostam de viver o momento presente sem se preocupar muito com o que está por vir. Preferem manter os relacionamentos leves e pacíficos, evitando situações conflitantes. Por serem ativas, gostam de dinamismo e não apreciam rotinas, mas sua possível superficialidade e descontração podem, contudo, exigir monitoramento em tarefas e prazos a cumprir.'
head_estavel = 'Estável'
body_estavel = 'As pessoas com o estilo Estável, assim como os Influentes, estão voltadas para os outros e para os relacionamentos interpessoais. Geralmente simpáticos, são de fácil convivência, afáveis e compreensivos, apresentando, comumente, uma preocupação com as necessidades alheias e dificuldade para dizer “não”. São bons ouvintes e flexíveis com suas ideias. Também são pacientes e, por isso, possuem disciplina e perseverança para seguir com o que foi planejado. A tranquilidade e a mansidão também ajudam a configurar este estilo reservado, introvertido e equilibrado, que pode também apresentar dificuldade para expressar seus sentimentos e tendência a guardar rancor. Buscam por segurança e estabilidade e, por isso, possuem um ritmo estável, gostam de rotinas e não costumam reagir bem às mudanças repentinas. Precisam de tempo para se adaptar. Para manter o ambiente harmônico e estável, buscam trabalhar em equipe por meio de consenso e em prol de um objetivo comum. Para isso, consideram importante receber orientações e deixar claro por meio de estruturas, planos e métodos o que cada pessoa da equipe irá fazer. Quando as regras do jogo estão claras, sentem-se bem em atuarem com pessoas mais dinâmicas e ativas.'
head_analitico = 'Analítico'
boody_analitico = 'Quem tem o estilo analítico como predominante é do tipo lógico, analítico e racional, que pensa de forma sistemática, baseada nos fatos, tomando decisões com cuidado, analisando todos os detalhes para que tudo saia correto. A sua busca por exatidão, contudo, vem acompanhada de rigidez e de preocupação. O hábito de sempre analisar todos os pontos de vistas antes de agir expressa um tom de pessimismo que também é sua característica. Os Analíticos apresentam-se como pessoas discretas, caladas e retraídas, mas comumente são reconhecidos por sua intelectualidade e habilidade com tarefas que exigem alta concentração e sensibilidade. Pelo fato de enxergarem muitos detalhes e informações que os outros estilos não conseguem ver, eles tendem a serem bons solucionadores de problemas e pessoas muito criativas, capazes de uma rápida improvisação. O seu alto grau de perfeccionismo pode estar relacionado com problemas de baixa autoestima, pois tendem a não admitir erros e estão sempre achando que o seu trabalho será imperfeito. Precisam, portanto, de estimulação, monitoramento e incentivos dos outros para vencerem o período de hesitação frente às tarefas e desafios. O medo de não serem aprovados podem travar o processo de execução e os deixam também mais sensíveis a eventuais críticas. Por outro lado, a combinação de sua sensibilidade, intelectualidade e tendência ao perfeccionismo os fazem ter padrões muito elevados, tanto para si mesmos, quanto para os outros.'

def perfil(head_perfil, body_perfil):
    perfil_head = head_perfil
    perfil_body = html.Div([
        dbc.Container([
            body_perfil
        ], className='laed')
    ])
    return perfil_head, perfil_body
