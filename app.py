from flask import Flask

from agentdoc.containers import Container

app = Flask(__name__)

TEXT = """
Austria's far-right Freedom Party is heading for an unprecedented general
election victory under leader Herbert Kickl, projections say.
The projections, based on initial results, give Kickl's party 28.9% - almost
three points ahead of the conservative People's Party on 26.23%, but far
short of a majority.
The Freedom Party (FPÖ) has been in coalition before, but the second-placed
conservative People's Party has refused to take part in a government
led by him.
Kickl's victory is only the latest in a string of far-right election successes
in Europe and he praised voters for their "optimism, courage and trust".
Kickl's main rival, incumbent Chancellor Karl Nehammer of the
People Party (ÖVP), has said it's “impossible to form a government with
someone who adores conspiracy theories”.
Some 6.3 million Austrians were eligible to vote in a race dominated
by the twin issues of migration and asylum, as well as inflation
and the war in Ukraine.
General secretary Michael Schnedlitz was delighted with the initial
projections, declaring that "the men and women of Austria have made
history today". He refused to say what kind of coalition his party
would try to build.
They are on course to secure about 57 seats in the 183-seat parliament,
with the conservatives on 52 and the Social Democrats on 41.
The Freedom Party's fiery leader, Herbert Kickl, has promised Austrians
to build "Fortress Austria", to restore their security, prosperity and peace,
and he has aligned himself closely with Viktor Orban in neighbouring Hungary.
"""


@app.route("/")
def hello_world():
    container = Container()

    chain = container.summarization_chain()
    result = chain.invoke(
        {
            "input_text": TEXT,
        },
    )

    return f"{result}"
