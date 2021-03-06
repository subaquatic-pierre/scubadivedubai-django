# Generated by Django 2.2.4 on 2019-12-10 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line_1', models.CharField(max_length=100)),
                ('address_line_2', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=100)),
                ('address_type', models.CharField(choices=[('B', 'Billing'), ('S', 'Shipping')], max_length=1)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(default='', editable=False, max_length=100)),
                ('image', models.ImageField(default='default_category.jpg', upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('sku', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField(blank=True, null=True)),
                ('stock_count', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='')),
                ('slug', models.SlugField(default='', editable=False, max_length=100)),
                ('description', models.TextField(default='Short Description here, all the items are the most amazing items one can find. Please take a minute to really appreciate everything around you. Without pain there could be no pleasure. Enjoy the pain for the pain carries the pleasure')),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('brand', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='shop.Brand')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='shop.Category')),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Color')),
            ],
        ),
        migrations.CreateModel(
            name='ItemInfo',
            fields=[
                ('title', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('heading', models.CharField(max_length=255)),
                ('text', models.TextField(default='This is default info on the item')),
            ],
            options={
                'verbose_name_plural': 'Item Info',
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(max_length=30, unique=True)),
                ('ordered', models.BooleanField(default=False)),
                ('start_date', models.DateField(auto_now=True)),
                ('ordered_date', models.DateField(blank=True, null=True)),
                ('on_delivery', models.BooleanField(default=False)),
                ('received', models.BooleanField(default=False)),
                ('refund_requested', models.BooleanField(default=False)),
                ('refund_granted', models.BooleanField(default=False)),
                ('billing_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_billing_address', to='shop.Address')),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Coupon')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ShopProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('stripe_customer_id', models.CharField(blank=True, max_length=50, null=True)),
                ('one_click_purchasing', models.BooleanField(default=False)),
                ('billing_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_address', to='shop.Address')),
                ('current_order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Order')),
                ('redeemend_coupons', models.ManyToManyField(blank=True, to='shop.Coupon')),
                ('shipping_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_address', to='shop.Address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('accepted', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254)),
                ('ref_code', models.CharField(max_length=30, unique=True)),
                ('username', models.CharField(max_length=255)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Order')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.ShopProfile', to_field='user')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_option', models.CharField(choices=[('stripe', 'Stripe'), ('paypal', 'Paypal'), ('cash', 'Cash')], max_length=20)),
                ('stipe_id_code', models.CharField(blank=True, max_length=50, null=True)),
                ('paypal_id_code', models.CharField(blank=True, max_length=50, null=True)),
                ('amount', models.FloatField()),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('ref_code', models.CharField(max_length=30, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.ShopProfile', to_field='user')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='shop.Order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Payment'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_shipping_address', to='shop.Address'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.ShopProfile', to_field='user'),
        ),
        migrations.AddField(
            model_name='item',
            name='item_info',
            field=models.ManyToManyField(blank=True, to='shop.ItemInfo'),
        ),
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Label'),
        ),
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Size'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.ShopProfile', to_field='user'),
        ),
    ]
