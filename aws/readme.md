### AWS Tutorials

## create user for ssh
```bash
sudo adduser new_user 
```
or
```bash
sudo adduser new_user --disabled-password
```
```bash
sudo usermod -aG sudo new_user
```
```bash
sudo su - new_user
```
```bash
mkdir .ssh
```
```bash
chmod 700 .ssh
```
```bash
echo "ssh-pub-key" > .ssh/authorized_keys
```
```bash
chmod 600 .ssh/authorized_keys
```
</br>

**AWS ECS Tutorials**
- [KodeKloud](https://youtu.be/esISkPlnxL0)

**AWS Lambda Tutorials**
- [KodeKloud](https://youtu.be/RtiWU1DrMaM)
- [Unfold Data Science](https://youtu.be/MUbaC5Hbm9g)
- [Soumil Shah](https://youtube.com/playlist?list=PLL2hlSFBmWwx5aS9AMYO-NndQITnEnqT4)

**AWS SageMaker Tutorials**
- [Unfold Data Science](https://youtu.be/agq-C4XyL3E)
- [Unfold Data Science](https://youtu.be/Bxo_DrPSJgI)

**AWS Machine Learning Playlist - Unfold Data Science**
- [YouTube Playlist](https://youtube.com/playlist?list=PLmPJQXJiMoUWFW2JxRSAfhcsQ0Cr9qbv-)

**Lambda, FastAPI, ECR**
- [Blog: FastAPI Container App Deployment using AWS Lambda and API Gateway](https://blog.searce.com/fastapi-container-app-deployment-using-aws-lambda-and-api-gateway-6721904531d0)

**Note:**
If you intend to store temporary data in Lambda, ensure it is stored in the location "/tmp"; otherwise, Lambda will throw an error.
