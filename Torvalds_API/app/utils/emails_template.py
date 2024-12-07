import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Utils:

    @staticmethod
    def template_academy(recipient_name: str, recipient_email: str) -> MIMEMultipart:

        template: MIMEMultipart = MIMEMultipart()
        
        template['From'] = os.getenv('SENDER_EMAIL')
        template['To'] = recipient_email
        template['Subject'] = "Linus Torvalds"
        
        template_body: str = f"""
        <html>
            <body>
                <h1>Hello!, {recipient_name}!</h1>
                <br /><br />
                <p style="padding: 12px; border-left: 4px solid #d0d0d0;">
                Linus Benedict Torvalds was born in Helsinki, Finland, on December 28, 1969. In 1988, he enrolled at the University of Helsinki to study Computer Science. This university was a pivotal choice due to its strong emphasis on technology and research, providing Linus with a solid foundation in programming and operating systems.
                <br /><br />
                During his undergraduate studies, Linus developed a keen interest in the Unix operating system, widely used in academic settings but accessible only on specific and costly platforms. To deepen his understanding, he experimented with Minix, an educational operating system, which later inspired the creation of the Linux kernel.
                br/><br />  
                Linus completed his Computer Science degree in 1996. His thesis, titled Linux: A Portable Operating System, offered a detailed analysis of the project he had initiated during his university years. The thesis explored the technical challenges, the principles of portability, and the advantages of creating an open and modular operating system. This academic work was not only a milestone in his education but also a demonstration of how academic projects can achieve global significance.
                <br /><br />
                Although Linus’s influence extended far beyond academia, his time at the University of Helsinki was instrumental in shaping his perspective on software and technology. In recognition of his contributions, the university awarded him an honorary Doctor of Science degree in 2000, underscoring the importance of his academic foundation in his groundbreaking career. 
                <br /><br />
                </p>
                <br />
                <div style='text-align: center'>
                    <img    src="https://lemelson.mit.edu/sites/default/files/inventor-image/torvaldsport.gif" alt="Torvalds" width="300" />
                </div>
                <br />
                <p>This email is sent from TorvaldsAPI!.</p>
                <a href="https://www.exemplo.com">Repository link: </a>
                <p>Give a Star to Help Me!</p>
                <p>Thanks!</p>
                <br />
                <a href="https://www.linkedin.com/in/felipe-fvieira/">contact me!</a>
                <br />
                <p>Yours sincerely,</p>
                <p><b>Felipe França</b></p>
            </body>
        </html>
        """

        template.attach(MIMEText(template_body, 'html'))
        
        return template
    @staticmethod
    def template_linux_creation(recipient_name: str, recipient_email: str) -> MIMEMultipart:

        template: MIMEMultipart = MIMEMultipart()
        
        template['From'] = os.getenv('SENDER_EMAIL')
        template['To'] = recipient_email
        template['Subject'] = "Linus Torvalds"
        
        template_body: str = f"""
        <html>
            <body>
                <h1>Hello!, {recipient_name}!</h1>
                <br />
                <p style="padding: 12px; border-left: 4px solid #d0d0d0;">
                Linux was created in the early 1990s as a personal project by Linus Torvalds, a Computer Science student at the University of Helsinki, Finland. Dissatisfied with the limitations of the educational operating system Minix, developed by Andrew S. Tanenbaum, and curious about the core principles of operating systems, Linus set out to create his own kernel (the core component of an operating system).
                <br /><br />
                <b>The Project’s Beginnings</b>
                <br /><br />
                In 1991, while using Minix for learning, Linus realized he wanted an operating system that could better meet his needs. Inspired by Unix, he began developing a new kernel as a hobby, using a computer powered by an Intel 80386 processor. His initial goal was to build a simple, functional, and portable system that could run on standard hardware.
                <br /><br />
                Linus first announced the project publicly on August 25, 1991, in a discussion forum called comp.os.minix. In his post, he wrote:
                <br /><br />
                <i>"I'm doing a (free) operating system (just a hobby, won't be big and professional like GNU) for 386(486) AT clones."</i>
                <br /><br />
                This announcement marked the beginning of what would become Linux.
                <br /><br />
                <b>First Version</b>
                <br /><br />
                The first official version of the Linux kernel, version 0.01, was released on September 17, 1991. This initial release contained only the kernel source code and had limited functionality—it lacked a graphical interface and was intended for experienced programmers.
                <br /><br />
                Shortly after, version 0.02 was released in October 1991, capable of running basic programs like the Bash shell and GCC, the compiler used to build the kernel. From this point, Linux began to gain traction among developers.
                <br /><br />
                <b>Collaboration and the Open Source Model</b>
                <br /><br />
                One of Linus's most significant decisions was to release Linux under the GNU General Public License (GPL) in 1992. This allowed anyone to use, study, modify, and redistribute the code, provided any improvements were shared under the same terms. This decision attracted a global community of programmers who started contributing to the project by adding features, fixing bugs, and adapting Linux for various platforms and use cases.
                <br /><br />
                Combined with the work of the Free Software Foundation (FSF), led by Richard Stallman, Linux became the ideal kernel for the GNU Project, which provided essential tools and libraries to create a complete operating system.
                <br /><br />
                <b>Growth and Evolution</b>
                <br /><br />
                Linux quickly evolved from Linus’s hobby to a cornerstone of modern technology. During the 1990s, it gained traction in server environments due to its stability and flexibility. With the emergence of distributions like Debian, Red Hat, and Slackware, Linux also found its way onto desktops.
                <br /><br />
                <b>Impact</b>
                <br /><br />
                Today, Linux is used in a vast range of devices, from servers and supercomputers to smartphones (via Android), IoT devices, and embedded systems. It powers most of the internet’s infrastructure and cloud computing environments. Linux stands as a symbol of the power of collaboration and open-source development.
                <br /><br />
                The project Linus Torvalds started continues to be managed by him and a global community, showcasing the transformative impact of software designed to be free and collaborative.
                <br /><br />
                </p>
                <br />
                <div style='text-align: center'>
                    <img src="https://lemelson.mit.edu/sites/default/files/inventor-image/torvaldsport.gif" alt="Torvalds" width="300" />
                </div>
                <br />
                <p>This email is sent from TorvaldsAPI!.</p>
                <a href="https://www.exemplo.com">Repository link: </a>
                <p>Give a Star to Help Me!</p>
                <p>Thanks!</p>
                <br />
                <a href="https://www.linkedin.com/in/felipe-fvieira/">contact me!</a>
                <br />
                <p>Yours sincerely,</p>
                <p><b>Felipe França</b></p>
            </body>
        </html>
        """

        template.attach(MIMEText(template_body, 'html'))
        
        return template
    @staticmethod
    def template_torvalds_biography(recipient_name: str, recipient_email: str) -> MIMEMultipart:

        template: MIMEMultipart = MIMEMultipart()
        
        template['From'] = os.getenv('SENDER_EMAIL')
        template['To'] = recipient_email
        template['Subject'] = "Linus Torvalds"
        
        template_body: str = f"""
        <html>
            <body>
                <h1>Hello!, {recipient_name}!</h1>
                <br />
                <p style="padding: 12px; border-left: 4px solid #d0d0d0;">
                Linus Benedict Torvalds was born on December 28, 1969, in Helsinki, Finland. He is globally renowned as the creator of the Linux kernel, one of the most significant open-source projects in history. Torvalds also played a pivotal role in the development of the Git version control system.
                <br /><br />
                <b>Early Life and Education</b>
                <br /><br />
                Linus grew up in an intellectual family; his parents, Anna and Nils Torvalds, were journalists and political activists. From an early age, he showed an interest in technology and programming, acquiring his first computer, a Commodore VIC-20, at the age of 11. During his teenage years, he honed his programming skills by creating simple games and computational tools.
                in 1988, he enrolled at the University of Helsinki, where he studied Computer Science. During his studies, he became fascinated with the Unix operating system, sparking his ambition to create a similar system accessible for personal computers.
                <br /><br />
                <b>reation of Linux</b>
                While at university, Linus began working on a personal project to develop a Unix-inspired operating system kernel. On August 25, 1991, he announced his project in a developer forum, inviting the community to collaborate. The project, initially called "Linux" (a blend of his name and Unix), quickly gained global support.
                <br /><br />
                inux was released under the GNU General Public License (GPL) in 1992, allowing anyone to use, modify, and redistribute it. This decision transformed Linux into a symbol of the free and open-source software movement, solidifying its role as a cornerstone of modern computing.
                <br /><br />
                <b>Contributions Beyond Linux</b>
                In addition to leading Linux development, Linus created Git in 2005, a version control system widely used for managing software development projects. Git has become an essential tool for programming teams worldwide.
                <br /><br />
                <b>Recognition and Impact</b>
                Linus Torvalds is celebrated as a central figure in computing history. He has received numerous awards and honors, including being named a Fellow of the Free Software Foundation and receiving the Millennium Technology Prize in 2012.
                <br /><br />
                Today, Linux powers everything from servers and supercomputers to mobile devices (via Android) and embedded systems. Torvalds continues to oversee the development of the Linux kernel, collaborating with a global developer community.
                <br /><br />
                <b>Personal Life</b>
                Linus is married to Tove Monni Torvalds, a karate champion. They have three daughters and reside in the United States. Although he is now a naturalized American citizen, Torvalds maintains a strong connection to his Finnish roots.
                </p>
                <br />
                <div style='text-align: center'>
                    <img src="https://lemelson.mit.edu/sites/default/files/inventor-image/torvaldsport.gif" alt="Torvalds" width="300" />
                </div>
                <br />
                <p>This email is sent from TorvaldsAPI!.</p>
                <a href="https://www.exemplo.com">Repository link: </a>
                <p>Give a Star to Help Me!</p>
                <p>Thanks!</p>
                <br />
                <a href="https://www.linkedin.com/in/felipe-fvieira/">contact me!</a>
                <br />
                <p>Yours sincerely,</p>
                <p><b>Felipe França</b></p>
            </body>
        </html>
        """

        template.attach(MIMEText(template_body, 'html'))
        
        return template